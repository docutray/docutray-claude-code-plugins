"""RAG Manager - Core logic for document vectorization and search using Qdrant + FastEmbed."""

import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, asdict

from fastembed import TextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue,
)


@dataclass
class DocumentMetadata:
    """Metadata for indexed documents."""
    doc_id: str
    title: str
    source_path: str
    file_type: str
    date_added: str
    chunk_index: int
    total_chunks: int
    word_count: int
    text: str  # Store original text for retrieval

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SearchResult:
    """Search result with relevance score."""
    doc_id: str
    title: str
    source_path: str
    chunk_text: str
    chunk_index: int
    score: float

    def __str__(self) -> str:
        return f"[{self.score:.3f}] {self.title} (chunk {self.chunk_index})"


class RAGManager:
    """Manages document vectorization and semantic search using Qdrant + FastEmbed."""

    COLLECTION_NAME = "rag_research_documents"
    METADATA_FILE = "documents_metadata.json"

    def __init__(
        self,
        db_path: Optional[str] = None,
        embedding_model: str = "BAAI/bge-small-en-v1.5",
        chunk_size: int = 512,
        chunk_overlap: int = 50,
    ):
        """
        Initialize RAG Manager.

        Args:
            db_path: Path to store Qdrant database (default: ~/.rag-research)
            embedding_model: FastEmbed model name
            chunk_size: Number of characters per chunk
            chunk_overlap: Overlap between chunks
        """
        self.db_path = Path(db_path) if db_path else Path.home() / ".rag-research"
        self.db_path.mkdir(parents=True, exist_ok=True)

        self.embedding_model_name = embedding_model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # Initialize FastEmbed model
        self._embedding_model = None

        # Initialize Qdrant client with local storage
        self.client = QdrantClient(path=str(self.db_path / "qdrant_data"))

        # Metadata storage
        self.metadata_path = self.db_path / self.METADATA_FILE
        self._documents_metadata: dict = self._load_metadata()

        # Ensure collection exists
        self._ensure_collection()

    @property
    def embedding_model(self) -> TextEmbedding:
        """Lazy initialization of embedding model."""
        if self._embedding_model is None:
            self._embedding_model = TextEmbedding(model_name=self.embedding_model_name)
        return self._embedding_model

    def _get_vector_size(self) -> int:
        """Get the embedding dimension from the model."""
        # BGE-small-en-v1.5 has 384 dimensions
        model_dims = {
            "BAAI/bge-small-en-v1.5": 384,
            "BAAI/bge-base-en-v1.5": 768,
            "BAAI/bge-large-en-v1.5": 1024,
        }
        return model_dims.get(self.embedding_model_name, 384)

    def _embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for texts using FastEmbed."""
        embeddings = list(self.embedding_model.embed(texts))
        return [e.tolist() for e in embeddings]

    def _load_metadata(self) -> dict:
        """Load documents metadata from disk."""
        if self.metadata_path.exists():
            return json.loads(self.metadata_path.read_text())
        return {"documents": {}, "stats": {"total_documents": 0, "total_chunks": 0}}

    def _save_metadata(self) -> None:
        """Save documents metadata to disk."""
        self.metadata_path.write_text(json.dumps(self._documents_metadata, indent=2))

    def _ensure_collection(self) -> None:
        """Ensure the vector collection exists."""
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]

        if self.COLLECTION_NAME not in collection_names:
            vector_size = self._get_vector_size()

            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

    def _generate_doc_id(self, source_path: str) -> str:
        """Generate unique document ID from source path."""
        return hashlib.md5(source_path.encode()).hexdigest()[:12]

    def _generate_point_id(self, doc_id: str, chunk_index: int) -> int:
        """Generate numeric point ID from doc_id and chunk index."""
        # Create a deterministic numeric ID from the string
        combined = f"{doc_id}_{chunk_index}"
        return int(hashlib.md5(combined.encode()).hexdigest()[:15], 16)

    def _chunk_text(self, text: str) -> list[str]:
        """Split text into overlapping chunks."""
        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = start + self.chunk_size
            chunk = text[start:end]

            # Try to break at sentence or word boundary
            if end < text_len:
                # Look for sentence end
                for sep in ['. ', '.\n', '\n\n', '\n', ' ']:
                    last_sep = chunk.rfind(sep)
                    if last_sep > self.chunk_size // 2:
                        chunk = chunk[:last_sep + len(sep)]
                        end = start + len(chunk)
                        break

            chunks.append(chunk.strip())
            start = end - self.chunk_overlap

        return [c for c in chunks if c]  # Filter empty chunks

    def add_document(
        self,
        text: str,
        source_path: str,
        title: Optional[str] = None,
        file_type: str = "unknown",
    ) -> str:
        """
        Add a document to the RAG database.

        Args:
            text: Document text content
            source_path: Original file path
            title: Document title (defaults to filename)
            file_type: File extension/type

        Returns:
            Document ID
        """
        doc_id = self._generate_doc_id(source_path)

        # Check if document already exists
        if doc_id in self._documents_metadata["documents"]:
            # Remove old chunks first
            self.remove_document(doc_id)

        # Use filename as title if not provided
        if not title:
            title = Path(source_path).stem

        # Chunk the document
        chunks = self._chunk_text(text)

        if not chunks:
            raise ValueError("Document produced no chunks after processing")

        # Generate embeddings for all chunks
        embeddings = self._embed_texts(chunks)

        # Prepare points for Qdrant
        points = []
        date_added = datetime.now().isoformat()

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            metadata = DocumentMetadata(
                doc_id=doc_id,
                title=title,
                source_path=source_path,
                file_type=file_type,
                date_added=date_added,
                chunk_index=i,
                total_chunks=len(chunks),
                word_count=len(chunk.split()),
                text=chunk,
            )

            point_id = self._generate_point_id(doc_id, i)
            points.append(
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload=metadata.to_dict(),
                )
            )

        # Upsert points to Qdrant
        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points,
        )

        # Update metadata
        self._documents_metadata["documents"][doc_id] = {
            "title": title,
            "source_path": source_path,
            "file_type": file_type,
            "date_added": date_added,
            "total_chunks": len(chunks),
            "word_count": len(text.split()),
        }
        self._documents_metadata["stats"]["total_documents"] += 1
        self._documents_metadata["stats"]["total_chunks"] += len(chunks)
        self._save_metadata()

        return doc_id

    def remove_document(self, doc_id: str) -> bool:
        """
        Remove a document from the RAG database.

        Args:
            doc_id: Document ID to remove

        Returns:
            True if document was removed, False if not found
        """
        if doc_id not in self._documents_metadata["documents"]:
            return False

        doc_info = self._documents_metadata["documents"][doc_id]

        # Delete points from Qdrant using filter
        self.client.delete(
            collection_name=self.COLLECTION_NAME,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="doc_id",
                        match=MatchValue(value=doc_id),
                    )
                ]
            ),
        )

        # Update metadata
        self._documents_metadata["stats"]["total_documents"] -= 1
        self._documents_metadata["stats"]["total_chunks"] -= doc_info["total_chunks"]
        del self._documents_metadata["documents"][doc_id]
        self._save_metadata()

        return True

    def list_documents(self, filter_term: Optional[str] = None) -> list[dict]:
        """
        List all indexed documents.

        Args:
            filter_term: Optional term to filter by title or path

        Returns:
            List of document metadata dictionaries
        """
        docs = list(self._documents_metadata["documents"].items())

        if filter_term:
            filter_lower = filter_term.lower()
            docs = [
                (doc_id, info) for doc_id, info in docs
                if filter_lower in info["title"].lower()
                or filter_lower in info["source_path"].lower()
            ]

        return [
            {"doc_id": doc_id, **info}
            for doc_id, info in docs
        ]

    def search(
        self,
        query: str,
        limit: int = 10,
        doc_ids: Optional[list[str]] = None,
    ) -> list[SearchResult]:
        """
        Search for relevant chunks using semantic similarity.

        Args:
            query: Search query
            limit: Maximum number of results
            doc_ids: Optional list of document IDs to search within

        Returns:
            List of SearchResult objects
        """
        # Generate query embedding
        query_embedding = self._embed_texts([query])[0]

        # Build filter if doc_ids specified
        query_filter = None
        if doc_ids:
            query_filter = Filter(
                should=[
                    FieldCondition(
                        key="doc_id",
                        match=MatchValue(value=doc_id),
                    )
                    for doc_id in doc_ids
                ]
            )

        # Search in Qdrant
        response = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=query_embedding,
            limit=limit,
            query_filter=query_filter,
            with_payload=True,
        )

        search_results = []
        for result in response.points:
            payload = result.payload
            search_results.append(SearchResult(
                doc_id=payload.get("doc_id", ""),
                title=payload.get("title", ""),
                source_path=payload.get("source_path", ""),
                chunk_text=payload.get("text", ""),
                chunk_index=payload.get("chunk_index", 0),
                score=result.score,
            ))

        return search_results

    def get_stats(self) -> dict:
        """Get database statistics."""
        return {
            "total_documents": self._documents_metadata["stats"]["total_documents"],
            "total_chunks": self._documents_metadata["stats"]["total_chunks"],
            "db_path": str(self.db_path),
            "embedding_model": self.embedding_model_name,
        }

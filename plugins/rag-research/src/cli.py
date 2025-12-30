#!/usr/bin/env python3
"""CLI for RAG Research - Document vectorization and search."""

import argparse
import os
import sys
import json
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from .rag_manager import RAGManager
from .document_loader import DocumentLoader


def get_manager() -> RAGManager:
    """Get configured RAG manager instance."""
    db_path = os.getenv("RAG_RESEARCH_DB_PATH") or None
    model = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
    chunk_size = int(os.getenv("CHUNK_SIZE", "512"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "50"))

    return RAGManager(
        db_path=db_path,
        embedding_model=model,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


def cmd_list(args):
    """List indexed documents."""
    manager = get_manager()
    docs = manager.list_documents(filter_term=args.filter)
    stats = manager.get_stats()

    if not docs:
        print("No documents indexed yet.")
        print(f"\nDatabase path: {stats['db_path']}")
        print("Use '/rag-research:add-doc <file>' to add documents.")
        return

    # Print header
    print("\n" + "=" * 100)
    print(f"{'ID':<14} {'Title':<35} {'Type':<6} {'Chunks':<8} {'Words':<8} {'Added':<12}")
    print("=" * 100)

    for doc in docs:
        title = doc["title"][:32] + "..." if len(doc["title"]) > 35 else doc["title"]
        date = doc["date_added"][:10]
        print(
            f"{doc['doc_id']:<14} {title:<35} {doc['file_type']:<6} "
            f"{doc['total_chunks']:<8} {doc['word_count']:<8} {date:<12}"
        )

    print("=" * 100)
    print(f"\nTotal: {len(docs)} documents | {stats['total_chunks']} chunks")
    print(f"Database: {stats['db_path']}")
    print(f"Model: {stats['embedding_model']}")


def cmd_add(args):
    """Add a document to the index."""
    file_path = args.file

    # Validate file
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    if not DocumentLoader.is_supported(file_path):
        print(f"Error: Unsupported file type: {Path(file_path).suffix}")
        print(f"Supported types: {', '.join(DocumentLoader.SUPPORTED_EXTENSIONS)}")
        sys.exit(1)

    print(f"Processing: {file_path}")

    # Load document
    loader = DocumentLoader(use_mistral_ocr=not args.no_ocr)
    try:
        text, file_type = loader.load(file_path)
    except Exception as e:
        print(f"Error loading document: {e}")
        sys.exit(1)

    if not text.strip():
        print("Error: Document appears to be empty")
        sys.exit(1)

    # Get title
    title = args.title or loader.get_title_from_file(file_path)

    # Add to index
    manager = get_manager()
    try:
        doc_id = manager.add_document(
            text=text,
            source_path=str(Path(file_path).resolve()),
            title=title,
            file_type=file_type,
        )
    except Exception as e:
        print(f"Error indexing document: {e}")
        sys.exit(1)

    # Get document info
    docs = manager.list_documents()
    doc_info = next((d for d in docs if d["doc_id"] == doc_id), None)

    print("\n" + "=" * 60)
    print("Document indexed successfully!")
    print("=" * 60)
    print(f"  ID:          {doc_id}")
    print(f"  Title:       {title}")
    print(f"  Type:        {file_type}")
    print(f"  Words:       {doc_info['word_count'] if doc_info else 'N/A'}")
    print(f"  Chunks:      {doc_info['total_chunks'] if doc_info else 'N/A'}")
    print(f"  Source:      {file_path}")
    print("=" * 60)


def cmd_remove(args):
    """Remove a document from the index."""
    manager = get_manager()

    if manager.remove_document(args.id):
        print(f"Document {args.id} removed successfully.")
    else:
        print(f"Document {args.id} not found.")
        sys.exit(1)


def cmd_research(args):
    """Search documents for a topic."""
    query = " ".join(args.query)

    if not query.strip():
        print("Error: Please provide a search query")
        sys.exit(1)

    manager = get_manager()
    stats = manager.get_stats()

    if stats["total_documents"] == 0:
        print("No documents indexed yet.")
        print("Use '/rag-research:add-doc <file>' to add documents first.")
        return

    print(f"\nSearching for: \"{query}\"")
    print(f"Searching across {stats['total_documents']} documents ({stats['total_chunks']} chunks)...\n")

    # Perform search
    results = manager.search(
        query=query,
        limit=args.limit,
    )

    if not results:
        print("No relevant results found.")
        print("\nTry:")
        print("  - Using different keywords")
        print("  - Adding more documents with /rag-research:add-doc")
        return

    # Group results by document
    docs_results = {}
    for result in results:
        if result.doc_id not in docs_results:
            docs_results[result.doc_id] = {
                "title": result.title,
                "source": result.source_path,
                "chunks": [],
            }
        docs_results[result.doc_id]["chunks"].append(result)

    # Output results
    print("=" * 100)
    print(f"Found {len(results)} relevant chunks across {len(docs_results)} documents")
    print("=" * 100)

    for doc_id, doc_data in docs_results.items():
        print(f"\n## [{doc_id}] {doc_data['title']}")
        print(f"   Source: {doc_data['source']}")
        print("-" * 80)

        for chunk in doc_data["chunks"]:
            # Truncate long chunks for display
            text = chunk.chunk_text
            if len(text) > 500:
                text = text[:500] + "..."

            print(f"\n   [Score: {chunk.score:.3f}] Chunk {chunk.chunk_index}:")
            # Indent the text
            indented = "\n".join(f"   {line}" for line in text.split("\n"))
            print(indented)

    print("\n" + "=" * 100)

    # Output as JSON for Claude to process
    if args.json:
        output = {
            "query": query,
            "total_results": len(results),
            "documents": len(docs_results),
            "results": [
                {
                    "doc_id": r.doc_id,
                    "title": r.title,
                    "source": r.source_path,
                    "chunk_index": r.chunk_index,
                    "score": r.score,
                    "text": r.chunk_text,
                }
                for r in results
            ],
        }
        print("\n--- JSON OUTPUT ---")
        print(json.dumps(output, indent=2))


def cmd_stats(args):
    """Show database statistics."""
    manager = get_manager()
    stats = manager.get_stats()

    print("\n" + "=" * 50)
    print("RAG Research Database Statistics")
    print("=" * 50)
    print(f"  Total Documents:  {stats['total_documents']}")
    print(f"  Total Chunks:     {stats['total_chunks']}")
    print(f"  Database Path:    {stats['db_path']}")
    print(f"  Embedding Model:  {stats['embedding_model']}")
    print("=" * 50)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="RAG Research - Document vectorization and search for Claude Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rag-research list                    # List all indexed documents
  rag-research list --filter mistral   # Filter by keyword
  rag-research add --file doc.pdf      # Add a document
  rag-research research machine learning  # Search for a topic
  rag-research remove --id abc123      # Remove a document
  rag-research stats                   # Show statistics
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list", help="List indexed documents")
    list_parser.add_argument("--filter", "-f", help="Filter by title or path")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a document to the index")
    add_parser.add_argument("--file", "-f", required=True, help="Path to document file")
    add_parser.add_argument("--title", "-t", help="Custom document title")
    add_parser.add_argument(
        "--no-ocr",
        action="store_true",
        help="Disable Mistral OCR for PDFs (use pypdf instead)",
    )

    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a document")
    remove_parser.add_argument("--id", required=True, help="Document ID to remove")

    # Research command
    research_parser = subparsers.add_parser("research", help="Search documents for a topic")
    research_parser.add_argument("query", nargs="+", help="Search query")
    research_parser.add_argument("--limit", "-l", type=int, default=10, help="Max results (default: 10)")
    research_parser.add_argument("--json", "-j", action="store_true", help="Output results as JSON")

    # Stats command
    subparsers.add_parser("stats", help="Show database statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Route to command handler
    commands = {
        "list": cmd_list,
        "add": cmd_add,
        "remove": cmd_remove,
        "research": cmd_research,
        "stats": cmd_stats,
    }

    try:
        commands[args.command](args)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

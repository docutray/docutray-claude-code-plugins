---
name: rag-research
description: Use this skill when users ask about RAG (Retrieval-Augmented Generation), semantic search, document indexing, embeddings, vector databases, or chunking strategies. Trigger phrases include "how does rag-research work", "improve search results", "RAG optimization", "embedding model", "chunking strategy", "vector database".
---

# RAG Research Skill

Use this skill when users ask about RAG (Retrieval-Augmented Generation), semantic search, document indexing, embeddings, vector databases, or chunking strategies. This skill provides best practices for working with the rag-research plugin and optimizing document retrieval.

## When to Use

Trigger this skill when users:
- Ask about RAG, embeddings, or semantic search concepts
- Want to optimize their document indexing strategy
- Need help with chunking or retrieval quality
- Ask "how does rag-research work?" or "how to improve search results?"
- Troubleshoot poor search results or missing information

## Core Concepts

### Document Indexing Pipeline

1. **Load Document**: Extract text from PDF, Markdown, or Text files
2. **Chunk Text**: Split into overlapping segments (default: 512 chars, 50 overlap)
3. **Generate Embeddings**: Convert chunks to vectors using FastEmbed (BAAI/bge-small-en-v1.5)
4. **Store in Qdrant**: Persist vectors with metadata for retrieval

### Embedding Models

The plugin uses FastEmbed with ONNX Runtime for efficient CPU inference:

| Model | Dimensions | Speed | Quality | Use Case |
|-------|------------|-------|---------|----------|
| `BAAI/bge-small-en-v1.5` | 384 | Fast | Good | Default, general use |
| `BAAI/bge-base-en-v1.5` | 768 | Medium | Better | Higher accuracy needs |
| `BAAI/bge-large-en-v1.5` | 1024 | Slow | Best | Maximum quality |

### Chunking Strategies

Chunk size affects retrieval quality:
- **Smaller chunks (256-512)**: More precise, may lose context
- **Larger chunks (1024+)**: More context, may dilute relevance
- **Overlap (10-20%)**: Prevents information loss at boundaries

Recommend: Start with defaults (512/50), adjust based on results.

### Search Quality Tips

1. **Use specific queries**: "Mistral OCR API configuration" > "OCR"
2. **Check coverage**: Run `/rag-research:list` to verify documents are indexed
3. **Increase limit**: Use `--limit 20` for comprehensive research
4. **Review scores**: Scores > 0.7 are highly relevant, < 0.5 may be tangential

## Troubleshooting

### Poor Search Results

1. **Check if document is indexed**: `/rag-research:list --filter "keyword"`
2. **Re-index with different chunking**: Adjust `CHUNK_SIZE` in `.env`
3. **Use more specific queries**: Add domain-specific terms
4. **Verify embeddings**: Check model compatibility

### PDF Extraction Issues

1. **Enable Mistral OCR**: Set `MISTRAL_API_KEY` in `.env` for scanned PDFs
2. **Fallback to pypdf**: Use `--no-ocr` flag for text-based PDFs
3. **Check file permissions**: Ensure PDF is readable

### Database Issues

1. **Reset database**: `rm -rf ~/.rag-research` and re-index
2. **Check disk space**: Qdrant needs space for vectors
3. **Verify installation**: `uv run rag-research stats`

## Configuration Reference

See `references/configuration.md` for detailed settings documentation.

## Examples

See `references/examples.md` for common usage patterns.

# RAG Research Configuration

## Environment Variables

Create a `.env` file in the plugin directory or set these environment variables:

```bash
# Required for PDF OCR (optional - falls back to pypdf)
MISTRAL_API_KEY="your-mistral-api-key"

# Database path (default: ~/.rag-research)
RAG_RESEARCH_DB_PATH="/custom/path/to/db"

# Embedding model (default: BAAI/bge-small-en-v1.5)
EMBEDDING_MODEL="BAAI/bge-small-en-v1.5"

# Chunking parameters
CHUNK_SIZE=512      # Characters per chunk (default: 512)
CHUNK_OVERLAP=50    # Overlap between chunks (default: 50)
```

## Settings File

Create `.claude/rag-research.local.md` in your project for project-specific configuration:

```markdown
# RAG Research Settings

## Embedding Model
Use `BAAI/bge-small-en-v1.5` for this project.

## Chunk Size
Use 1024 character chunks for long-form documents.

## Custom Database Path
Store vectors in `./data/vectors/` for this project.
```

## Model Selection Guide

### BAAI/bge-small-en-v1.5 (Default)
- **Dimensions**: 384
- **Size**: ~50MB
- **Speed**: ~1000 chunks/second on CPU
- **Best for**: Most use cases, quick indexing

### BAAI/bge-base-en-v1.5
- **Dimensions**: 768
- **Size**: ~110MB
- **Speed**: ~500 chunks/second on CPU
- **Best for**: Technical documentation, code

### BAAI/bge-large-en-v1.5
- **Dimensions**: 1024
- **Size**: ~335MB
- **Speed**: ~200 chunks/second on CPU
- **Best for**: Research papers, complex queries

## Chunk Size Recommendations

| Document Type | Chunk Size | Overlap | Rationale |
|---------------|------------|---------|-----------|
| Technical docs | 512 | 50 | Balance of precision and context |
| Research papers | 1024 | 100 | Preserve paragraph context |
| Code files | 256 | 25 | Function-level granularity |
| Long-form content | 768 | 75 | Section-level retrieval |

## Database Management

### Backup
```bash
cp -r ~/.rag-research ~/.rag-research.backup
```

### Migrate
```bash
# Export document list
uv run rag-research list > documents.txt
# Clear and re-index
rm -rf ~/.rag-research
# Re-add documents
```

### Multiple Projects
Use `RAG_RESEARCH_DB_PATH` to maintain separate databases:
```bash
RAG_RESEARCH_DB_PATH=./project-a-vectors uv run rag-research add --file doc.pdf
RAG_RESEARCH_DB_PATH=./project-b-vectors uv run rag-research add --file other.pdf
```

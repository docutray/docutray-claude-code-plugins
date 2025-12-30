# RAG Research Configuration

## Database Location

By default, the database is stored in `.rag-research/` within your current project directory. This provides project-isolated document indexes.

**Priority order:**
1. `RAG_RESEARCH_DB_PATH` environment variable (if set)
2. `<project>/.rag-research/` (project-local, default)
3. `~/.rag-research/` (fallback if no project context)

The `.rag-research/` directory is automatically added to your project's `.gitignore`.

## Environment Variables

Create a `.env` file in the plugin directory or set these environment variables:

```bash
# Required for PDF OCR (optional - falls back to pypdf)
MISTRAL_API_KEY="your-mistral-api-key"

# Override database path (default: project-local .rag-research/)
RAG_RESEARCH_DB_PATH=""

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

Each project automatically gets its own database in `.rag-research/`. Simply run commands from different project directories:

```bash
# In project A - uses project-a/.rag-research/
cd /path/to/project-a
/rag-research:add-doc ./doc.pdf

# In project B - uses project-b/.rag-research/
cd /path/to/project-b
/rag-research:add-doc ./other.pdf
```

To share a database across projects, use `RAG_RESEARCH_DB_PATH`:
```bash
RAG_RESEARCH_DB_PATH=/shared/vectors uv run rag-research add --file doc.pdf
```

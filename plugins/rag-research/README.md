# RAG Research Plugin

RAG-based reference document management for Claude Code. Index documents and search them semantically to find relevant information for research topics.

## Installation

### From Docutray Marketplace

```bash
# Add marketplace (if not already added)
/plugin marketplace add docutray/docutray-claude-code-plugins

# Install plugin
/plugin install rag-research@docutray-plugins
```

### Setup Dependencies

After installation, sync Python dependencies:

```bash
cd ~/.claude/plugins/marketplaces/docutray-plugins/plugins/rag-research
uv sync
```

### Local Development

```bash
cd plugins/rag-research
uv sync
```

## Features

- **Document Indexing**: PDF, Markdown, Text, JSON support
- **Semantic Search**: FastEmbed embeddings + Qdrant vector store
- **Project-Local Storage**: Database stored in `.rag-research/` per project (auto-added to `.gitignore`)
- **PDF OCR**: Mistral AI integration for scanned documents
- **Deep Research**: Autonomous agent for comprehensive topic research
- **Configurable**: Customizable chunking, models, and database location

## Quick Start

```bash
# Add a document
/rag-research:add-doc ./docs/manual.pdf

# List indexed documents
/rag-research:list

# Search for information
/rag-research:research "your topic here"
```

## Claude Code Commands

| Command | Description |
|---------|-------------|
| `/rag-research:add-doc <file>` | Index a document |
| `/rag-research:list [filter]` | List all indexed documents |
| `/rag-research:research <topic>` | Search documents semantically |

## CLI Commands

```bash
# List documents
uv run rag-research list
uv run rag-research list --filter "keyword"

# Add documents
uv run rag-research add --file ./document.pdf
uv run rag-research add --file ./notes.md --title "Custom Title"
uv run rag-research add --file ./doc.pdf --no-ocr  # Skip Mistral OCR

# Research topics
uv run rag-research research "your search query"
uv run rag-research research "topic" --limit 20
uv run rag-research research "topic" --json

# Database management
uv run rag-research stats
uv run rag-research remove --id <doc_id>
```

## Configuration

### Database Location

By default, the database is stored in `.rag-research/` within your current project directory. This allows each project to have its own isolated document index.

**Priority order:**
1. `RAG_RESEARCH_DB_PATH` environment variable (if set)
2. `<project>/.rag-research/` (project-local, default)
3. `~/.rag-research/` (fallback if no project context)

The `.rag-research/` directory is automatically added to your project's `.gitignore`.

### Environment Variables

Create `.env` in the plugin directory:

```bash
# PDF OCR (optional - falls back to pypdf)
MISTRAL_API_KEY="your-mistral-api-key"

# Override database location (default: project-local .rag-research/)
RAG_RESEARCH_DB_PATH=""

# Embedding model (default: BAAI/bge-small-en-v1.5)
EMBEDDING_MODEL="BAAI/bge-small-en-v1.5"

# Chunking (defaults: 512/50)
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

### Project Settings

Create `.claude/rag-research.local.md` for project-specific configuration.

## Components

### Commands
- **add-doc**: Index documents with automatic chunking and embedding
- **list**: List indexed documents with filtering
- **research**: Semantic search with relevance scoring

### Skills
- **rag-research**: Knowledge base for RAG best practices, chunking strategies, and troubleshooting

### Agents
- **deep-researcher**: Autonomous agent for comprehensive research across multiple documents

## Technical Stack

| Component | Technology |
|-----------|------------|
| Vector Store | Qdrant (local mode) |
| Embeddings | FastEmbed (ONNX Runtime) |
| Default Model | BAAI/bge-small-en-v1.5 (384 dims) |
| PDF OCR | Mistral AI / pypdf fallback |
| Package Manager | uv |

## Troubleshooting

### Poor Search Results
1. Check indexed documents: `/rag-research:list`
2. Use more specific query terms
3. Increase result limit: `--limit 20`
4. Consider re-indexing with different chunk size

### PDF Extraction Issues
1. Set `MISTRAL_API_KEY` for scanned PDFs
2. Use `--no-ocr` for text-based PDFs
3. Check file permissions

### Database Reset
```bash
# For project-local database
rm -rf .rag-research
# Database reinitializes on next command

# For global database (if using RAG_RESEARCH_DB_PATH)
rm -rf ~/.rag-research
```

## License

MIT

## Support

- **Issues**: [GitHub Issues](https://github.com/docutray/docutray-claude-code-plugins/issues)
- **Marketplace**: [docutray-claude-code-plugins](https://github.com/docutray/docutray-claude-code-plugins)

---
description: Add a document to the RAG Research database for semantic search
argument-hint: "<filepath>"
allowed-tools: Read, Bash(uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research:*)
---

# Add Document to RAG Research

Index a document into the RAG Research database. The document will be chunked, embedded using FastEmbed (BAAI/bge-small-en-v1.5), and stored in Qdrant for semantic search.

## Supported File Types

- **PDF** (.pdf) - Extracted using Mistral OCR API (with pypdf fallback)
- **Markdown** (.md, .markdown) - Parsed directly
- **Text** (.txt, .rst) - Read as plain text
- **JSON** (.json) - Formatted and indexed

## Instructions

1. Verify the file exists and is a supported type
2. Run the add command: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research add --file "$ARGUMENTS"`
3. For custom title: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research add --file "$ARGUMENTS" --title "Custom Title"`
4. Report the document ID and indexing details

## Command Examples

```bash
# Add a PDF document
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research add --file "/path/to/guide.pdf"

# Add with custom title
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research add --file "./notes.md" --title "Research Notes"

# Add without Mistral OCR (use pypdf for PDFs)
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research add --file "./doc.pdf" --no-ocr
```

## Processing Details

1. **Text Extraction**: Content is extracted based on file type
2. **Chunking**: Text is split into ~512 character chunks with 50 char overlap
3. **Embedding**: Each chunk is embedded using FastEmbed (ONNX-based, fast)
4. **Storage**: Vectors and metadata stored in local Qdrant database

## Output

After successful indexing:
- Document ID (use this for research and removal)
- Title
- File type
- Word count
- Number of chunks created
- Source file path

## Usage Scenarios

- `/rag-research:add-doc ./data/documentation/framework.pdf`
- `/rag-research:add-doc ../research/notes.md`
- `/rag-research:add-doc ./specs/api-spec.json`

## Notes

- Documents are deduplicated by source path (re-adding updates the index)
- PDF OCR requires MISTRAL_API_KEY in .env (falls back to pypdf without it)
- Large documents may take a moment to process

---
description: List all documents indexed in the RAG Research database
argument-hint: "[filter]"
allowed-tools: Bash(uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research:*)
---

# List Reference Documents

List all documents that have been indexed in the RAG Research database. Optionally filter by a search term that matches document titles or paths.

## Instructions

1. Run the list command: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research list`
2. If a filter term is provided: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research list --filter "$ARGUMENTS"`
3. Display the results in a clear format

## Command Examples

```bash
# List all documents
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research list

# Filter by keyword
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research list --filter "mistral"
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research list --filter "pdf"
```

## Output Format

The command displays:
- **ID**: Unique document identifier (for use with other commands)
- **Title**: Document title
- **Type**: File format (pdf, md, txt)
- **Chunks**: Number of text chunks indexed
- **Words**: Total word count
- **Added**: Date when document was indexed

## Usage Scenarios

- `/rag-research:list` - Show all indexed documents
- `/rag-research:list mistral` - Show documents with "mistral" in title/path
- `/rag-research:list awp` - Show AWP-related documents

---
description: Research a topic using semantic search across indexed documents
argument-hint: "<topic>"
allowed-tools: Bash(uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research:*)
---

# Research Topic with RAG

Search your indexed reference documents using semantic similarity to find relevant information about a specific topic. This command uses retrieval-augmented generation (RAG) to find the most relevant chunks from your document collection.

## How It Works

1. Your query is embedded using the same FastEmbed model as documents
2. Qdrant performs cosine similarity search across all indexed chunks
3. Top matching chunks are returned with relevance scores
4. Results are grouped by source document for context

## Instructions

1. Run the research command: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research $ARGUMENTS`
2. For more results: `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research $ARGUMENTS --limit 20`
3. For JSON output (easier parsing): `uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research $ARGUMENTS --json`
4. Analyze the results and synthesize findings for the user

## Command Examples

```bash
# Basic research query
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research "document text extraction methods"

# Get more results
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research "OCR document processing" --limit 20

# JSON output for detailed analysis
uv run --directory ${CLAUDE_PLUGIN_ROOT} rag-research --project-dir "$PWD" research "project management best practices" --json
```

## Understanding Results

Each result includes:
- **Document ID & Title**: Source document reference
- **Score**: Semantic similarity (0-1, higher = more relevant)
- **Chunk Index**: Position in original document
- **Text**: The relevant excerpt

## Synthesizing Research

After getting results, you should:
1. **Identify key themes** across multiple chunks
2. **Cross-reference** information from different documents
3. **Note source documents** for citations
4. **Highlight gaps** if relevant information isn't found
5. **Suggest follow-ups** like adding more documents if needed

## Research Output Format

Present findings as:

```
## Research: [Topic]

### Key Findings
- Main point 1 (from Document X)
- Main point 2 (from Document Y)

### Detailed Excerpts
[Relevant quotes with source attribution]

### Sources Referenced
- [doc_id] Document Title
- [doc_id] Another Document

### Gaps & Recommendations
- Topics not covered in current documents
- Suggested documents to add
```

## Usage Scenarios

- `/rag-research:research mistral ocr api usage`
- `/rag-research:research PDF text extraction techniques`
- `/rag-research:research document extraction methods`

## Tips for Better Results

- Use specific terminology from your domain
- Try multiple phrasings if initial results are poor
- Use `--limit 20` for comprehensive research
- Check document coverage with `/rag-research:list` first

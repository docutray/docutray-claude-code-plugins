# RAG Research Usage Examples

## Basic Workflow

### 1. Index Your Documents

```bash
# Add a single PDF
uv run rag-research add --file ./docs/manual.pdf

# Add with custom title
uv run rag-research add --file ./notes/research.md --title "Q4 Research Notes"

# Add multiple documents
for f in ./papers/*.pdf; do
  uv run rag-research add --file "$f"
done
```

### 2. Verify Indexing

```bash
# List all documents
uv run rag-research list

# Filter by keyword
uv run rag-research list --filter "research"

# Check statistics
uv run rag-research stats
```

### 3. Research Topics

```bash
# Basic search
uv run rag-research research "machine learning optimization"

# Get more results
uv run rag-research research "API authentication patterns" --limit 20

# JSON output for processing
uv run rag-research research "database design" --json
```

## Advanced Patterns

### Research with Context Building

```bash
# Start broad
uv run rag-research research "authentication"

# Then narrow down based on results
uv run rag-research research "OAuth 2.0 token refresh flow"

# Deep dive on specific topic
uv run rag-research research "refresh token expiration handling" --limit 15
```

### Document Management

```bash
# Remove outdated document
uv run rag-research remove --id abc123def456

# Update document (remove + add)
uv run rag-research remove --id abc123def456
uv run rag-research add --file ./docs/manual-v2.pdf
```

### Integration with Claude Code

In Claude Code, use the slash commands:

```
/rag-research:list
/rag-research:add-doc ./path/to/document.pdf
/rag-research:research how to implement feature X
```

## Real-World Scenarios

### Scenario 1: Technical Documentation Research

You have 50+ PDF manuals and need to find specific configuration options:

```bash
# Index all manuals
for f in ./manuals/*.pdf; do
  uv run rag-research add --file "$f"
done

# Search for configuration
uv run rag-research research "network timeout configuration" --limit 20
```

### Scenario 2: Code Review Context

Need context from design documents while reviewing code:

```bash
# Index design docs
uv run rag-research add --file ./docs/architecture.md
uv run rag-research add --file ./docs/api-spec.json

# Search for relevant patterns
uv run rag-research research "error handling strategy"
```

### Scenario 3: Research Paper Analysis

Analyzing multiple research papers on a topic:

```bash
# Index papers with meaningful titles
uv run rag-research add --file ./papers/smith2024.pdf --title "Smith 2024 - ML Optimization"
uv run rag-research add --file ./papers/jones2023.pdf --title "Jones 2023 - Neural Networks"

# Cross-reference findings
uv run rag-research research "gradient descent improvements" --limit 25
```

## Troubleshooting Examples

### No Results Found

```bash
# Check what's indexed
uv run rag-research list

# Try broader terms
uv run rag-research research "authentication"  # Instead of "OAuth2 PKCE flow"

# Check with filter
uv run rag-research list --filter "auth"
```

### Poor Result Quality

```bash
# Use more specific domain terms
uv run rag-research research "React useEffect cleanup function memory leak"

# Increase result limit
uv run rag-research research "memory management" --limit 30

# Check scores in output - focus on results > 0.6
```

### Re-indexing with Different Settings

```bash
# Backup current state
uv run rag-research list > indexed-docs.txt

# Clear database
rm -rf ~/.rag-research

# Set new chunk size
export CHUNK_SIZE=1024
export CHUNK_OVERLAP=100

# Re-index
uv run rag-research add --file ./docs/long-document.pdf
```

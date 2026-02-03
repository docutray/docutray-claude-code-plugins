---
name: devflow-check
description: Execute all project validations in parallel including tests, linting, type checking, and build. Use when users want to validate code quality or check project health. Trigger phrases: "run tests", "validate code", "check quality", "/check", "run validations", "verify build"
type: flow
---

# DevFlow: Quality Validation Flow

Execute all project validations in parallel using specialized subagents, providing structured reporting of results.

## When to Use

Use this flow when you need to:
- Validate code quality before PR
- Check project health
- Run all tests and validations
- Verify build integrity
- Ensure no regressions

## Flow Diagram

```mermaid
flowchart TD
    A([BEGIN]) --> B[Parse arguments: --fast, --verbose]
    B --> C[Load project validation config]
    C --> D[Identify enabled validations]
    D --> E{Fast mode?}
    E -->|Yes| F[Skip build validation]
    E -->|No| G[Include all validations]
    F --> H[Launch parallel subagents]
    G --> H
    H --> I[test-runner: Execute tests]
    H --> J[lint-runner: Execute linting]
    H --> K[typecheck-runner: Type check]
    H --> L{Fast mode?}
    L -->|No| M[build-runner: Execute build]
    L -->|Yes| N[Skip build]
    I --> O[Collect JSON responses]
    J --> O
    K --> O
    M --> O
    N --> O
    O --> P[Aggregate results]
    P --> Q{All passed?}
    Q -->|No| R{Verbose mode?}
    R -->|Yes| S[Show full error details]
    R -->|No| T[Show summary with fix recommendations]
    Q -->|Yes| U[Generate success report]
    S --> V([END])
    T --> V
    U --> V
```

## Node Details

### 1. Load Configuration
Read `.claude/details/commands/check.md` for project-specific validation commands.

### 2. Parallel Execution
Launch all validation subagents simultaneously:
- **Tests**: Run complete test suite
- **Linting**: Code quality checks
- **Type Checking**: Language-specific type validation
- **Build**: Compile project (unless --fast)

### 3. Result Aggregation
Each subagent returns structured JSON:
```json
{
  "validation": "tests",
  "status": "success|warning|error",
  "duration": 12.3,
  "summary": "145 tests passed",
  "details": "...",
  "errors": [],
  "warnings": []
}
```

### 4. Executive Report
Generate consolidated summary with:
- Status per validation
- Execution time
- Error/warning count
- Recommended actions

## Parameters

- `--fast`: Skip build validation (quicker)
- `--verbose`: Show full output from all validations

## Example Usage

```
/flow:devflow-check
/flow:devflow-check --fast
/flow:devflow-check --verbose
```

## Output

Executive summary table:
```
┌─────────────────┬─────────┬─────────┬──────────────────────┐
│ Validation      │ Status  │ Time    │ Result               │
├─────────────────┼─────────┼─────────┼──────────────────────┤
│ 🧪 Tests        │ ✅ OK   │ 12.3s   │ 145 passed           │
│ 🔍 Linting      │ ⚠️ WARN │ 3.4s    │ 3 warnings           │
│ 📝 Type Check   │ ✅ OK   │ 8.5s    │ No type errors       │
│ 🏗️ Build        │ ✅ OK   │ 45.2s   │ Success              │
└─────────────────┴─────────┴─────────┴──────────────────────┘
```

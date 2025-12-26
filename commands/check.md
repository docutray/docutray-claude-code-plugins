---
description: "Execute all project validations using parallel subagents: tests, linting, type checking, and build"
allowed-tools:
  - Task
  - Bash(echo:*)
  - Read
argument-hints:
  - "--fast (skip build)"
  - "--verbose (show full output)"
---

# Check Command

Execute all project validations in parallel using specialized subagents, providing structured reporting of results.

## Usage

```bash
/check              # Execute all validations
/check --fast       # Only tests, linting, and type checking (skip build)
/check --verbose    # Show full output from each task
```

## Objective

Execute all critical project validations in parallel:
- 🧪 **Tests**: Run complete test suite
- 🔍 **Linting**: Verify code quality
- 📝 **Type Checking**: Validate types (language-specific)
- 🏗️ **Build**: Compile complete project (optional with --fast)

Optional (repo-specific):
- 📄 **OpenSpec**: Validate and/or archive an OpenSpec change before opening a PR

**Note**: Specific commands are configured per project in `.claude/details/commands/check.md`

## Instructions for Claude

**IMPORTANT - Parallel execution with subagents**

### Execution Flow

1. **Load Configuration**: Read `.claude/details/commands/check.md` for project-specific commands
2. **Argument Analysis**: Determine which validations to run
3. **Parallel Execution**: Launch all subagents simultaneously
4. **Result Aggregation**: Consolidate JSON responses from subagents
5. **Executive Report**: Show visual and detailed summary

### Detailed Process

#### 1. Load Project Configuration

**CRITICAL**: Before executing, read project-specific commands from:
`.claude/details/commands/check.md`

This file must define:
```json
{
  "validations": {
    "tests": {
      "command": "npm run test",
      "description": "Run test suite",
      "enabled": true
    },
    "lint": {
      "command": "npm run lint",
      "description": "Code quality validation",
      "enabled": true
    },
    "typecheck": {
      "command": "npm run type-check",
      "description": "Type validation",
      "enabled": true
    },
    "build": {
      "command": "npm run build",
      "description": "Project compilation",
      "enabled": true,
      "skip_on_fast": true
    }
  }
}
```

### OpenSpec integration (optional)

If the repo uses OpenSpec (i.e., it has an `openspec/` directory), you can include OpenSpec as validations in `.claude/details/commands/check.md`.

Common pattern: derive the change name from the current branch and run `openspec validate` and/or `openspec archive`.

Example validations:

```json
{
  "validations": {
    "openspec_validate": {
      "command": "CHANGE=$(git branch --show-current | sed 's|.*/||'); test -d openspec/changes/$CHANGE && openspec validate $CHANGE",
      "description": "Validate OpenSpec change format for current branch",
      "enabled": false
    },
    "openspec_archive": {
      "command": "CHANGE=$(git branch --show-current | sed 's|.*/||'); test -d openspec/changes/$CHANGE && openspec archive $CHANGE --yes",
      "description": "Archive OpenSpec change (pre-PR gate)",
      "enabled": false
    }
  }
}
```

Notes:
- This assumes your branch name (suffix) matches the change folder name under `openspec/changes/`.
- If your team uses a different naming convention, set `command` accordingly.

**Framework Examples**:

TypeScript/JavaScript:
```json
{
  "validations": {
    "tests": {"command": "npm run test"},
    "lint": {"command": "npm run lint"},
    "typecheck": {"command": "npx tsc --noEmit"},
    "build": {"command": "npm run build"}
  }
}
```

Python:
```json
{
  "validations": {
    "tests": {"command": "pytest"},
    "lint": {"command": "flake8 . && black --check ."}
  }
}
```

Go:
```json
{
  "validations": {
    "tests": {"command": "go test ./..."},
    "lint": {"command": "golangci-lint run"},
    "build": {"command": "go build ./..."}
  }
}
```

#### 2. Initial Preparation

```bash
# Show process start
echo "🚀 STARTING PROJECT VALIDATIONS"
echo ""
echo "📋 Scheduled validations:"
# List enabled validations from config
echo ""
echo "⏳ Executing in parallel..."
echo ""
```

#### 3. Parallel Subagent Execution

**CRITICAL**: Use Task tool to execute ALL subagents in parallel in a single invocation:

```markdown
Use the Task tool with multiple concurrent calls:

For each enabled validation in config:
- <validation-name>-runner subagent: "Execute <command> and provide structured JSON report"

Example for TypeScript project:
- test-runner subagent: "Execute npm run test and provide structured JSON report"
- lint-runner subagent: "Execute npm run lint and provide structured JSON report"
- typecheck-runner subagent: "Execute npx tsc --noEmit and provide structured JSON report"
- build-runner subagent: "Execute npm run build and provide structured JSON report" (unless --fast)

IMPORTANT: Launch all subagents in a SINGLE message with multiple Task tool calls for parallel execution.
```

**Subagent Response Format**:
Each subagent should return JSON:
```json
{
  "validation": "tests",
  "status": "success|warning|error",
  "duration": 12.3,
  "summary": "145 tests passed",
  "details": "Full output...",
  "errors": [],
  "warnings": []
}
```

#### 4. Result Processing

Once all JSON responses received:

1. **Parse JSON responses** from each subagent
2. **Calculate total metrics**:
   - Total time (maximum of all subagents)
   - General status (success only if all pass)
   - Error/warning count by category

3. **Generate consolidated report**

#### 5. Output Format

**During Execution**
```
🚀 STARTING PROJECT VALIDATIONS

📋 Scheduled validations:
  🧪 Tests - Running test suite
  🔍 Linting - Verifying code quality
  📝 Type Checking - Type validation
  🏗️ Build - Compiling project

⏳ Executing in parallel...

✅ Linting completed (3.4s)
✅ Type Checking completed (8.5s)
✅ Tests completed (12.3s)
✅ Build completed (45.2s)
```

**Final Report - Success Case**
```
✅ ALL VALIDATIONS COMPLETED

📊 Executive Summary:
┌─────────────────┬─────────┬─────────┬──────────────────────┐
│ Validation      │ Status  │ Time    │ Result               │
├─────────────────┼─────────┼─────────┼──────────────────────┤
│ 🧪 Tests        │ ✅ OK   │ 12.3s   │ 145 passed           │
│ 🔍 Linting      │ ⚠️  WARN│ 3.4s    │ 3 warnings           │
│ 📝 Type Check   │ ✅ OK   │  8.5s   │ No type errors       │
│ 🏗️ Build        │ ✅ OK   │ 45.2s   │ Success              │
└─────────────────┴─────────┴─────────┴──────────────────────┘

⏱️  Total time: 45.2s (executed in parallel)
🎯 General status: ✅ SUCCESS

Validations completed successfully. Project is ready.
```

**Final Report - Failure Case**
```
❌ VALIDATIONS FAILED

📊 Executive Summary:
┌─────────────────┬─────────┬─────────┬──────────────┐
│ Validation      │ Status  │ Time    │ Result       │
├─────────────────┼─────────┼─────────┼──────────────┤
│ 🧪 Tests        │ ❌ FAIL │ 8.1s    │ 12 failed    │
│ 🔍 Linting      │ ✅ OK   │ 3.4s    │ No issues    │
│ 📝 Type Check   │ ❌ FAIL │ 5.2s    │ 5 errors     │
│ 🏗️ Build        │ ❌ FAIL │ 15.7s   │ Build failed │
└─────────────────┴─────────┴─────────┴──────────────┘

⏱️  Total time: 15.7s (executed in parallel)
🎯 General status: ❌ ERRORS FOUND

🔧 Recommended actions:
  • Review failed tests in test suite
  • Resolve type errors
  • Fix build problems

For complete details, use: /check --verbose
```

#### 6. Verbose Mode

If `--verbose` specified, also show:

```
📋 COMPLETE DETAILS

🧪 TESTS:
[Raw output from test-runner subagent]

🔍 LINTING:
[Raw output from lint-runner subagent]

📝 TYPE CHECKING:
[Raw output from typecheck-runner subagent]

🏗️ BUILD:
[Raw output from build-runner subagent]
```

### Argument Handling

- **No arguments**: Execute all validations
- **--fast**: Skip build (only tests, lint, type-check) - useful for rapid development
- **--verbose**: Show full output in addition to summary
- **Invalid arguments**: Show usage help

### Technical Considerations

#### Effective Parallelization
- Use Task tool with multiple simultaneous invocations
- Don't wait for sequential subagent responses
- Calculate total time as maximum, not sum

#### Error Handling
- If subagent doesn't respond, report as "TIMEOUT"
- If subagent returns invalid format, report as "ERROR"
- Continue with other subagents even if some fail

#### Framework Flexibility
- Commands are defined per project in details file
- Different frameworks require different validations
- Some validations may not apply to all projects
- Easy addition of custom validations

### User Output

**Real-time During Execution**
```
🚀 STARTING PROJECT VALIDATIONS
⏳ Executing tests, linting, type checking and build in parallel...

✅ Linting completed (3.1s)
✅ Type Checking completed (7.2s)
✅ Tests completed (8.7s)
✅ Build completed (45.2s)

📊 Generating final report...
```

**Possible States per Task**
- ✅ OK: Task completed successfully
- ⚠️ WARN: Completed with warnings (only for linting)
- ❌ FAIL: Task failed with errors
- ⏸️ SKIP: Task omitted (e.g. build with --fast)
- ❓ ERROR: Unexpected error in subagent

## Project Customization

**REQUIRED**: Each project MUST configure validation commands in:
`.claude/details/commands/check.md`

This file should include:
- Specific commands for each validation
- Validation descriptions
- Which validations are enabled
- Framework-specific configuration
- Custom validations if needed

**Example for TypeScript/Node.js**:
```json
{
  "validations": {
    "tests": {
      "command": "npm run test",
      "description": "Jest test suite",
      "enabled": true
    },
    "lint": {
      "command": "npm run lint",
      "description": "ESLint validation",
      "enabled": true
    },
    "typecheck": {
      "command": "npx tsc --noEmit",
      "description": "TypeScript strict validation",
      "enabled": true
    },
    "build": {
      "command": "npm run build",
      "description": "Next.js build",
      "enabled": true,
      "skip_on_fast": true
    }
  }
}
```

**Example for Python**:
```json
{
  "validations": {
    "tests": {
      "command": "pytest -v",
      "description": "Pytest suite",
      "enabled": true
    },
    "lint": {
      "command": "flake8 . && black --check . && isort --check .",
      "description": "Code quality (flake8, black, isort)",
      "enabled": true
    },
    "typecheck": {
      "command": "mypy .",
      "description": "Type checking with mypy",
      "enabled": true
    }
  }
}
```

**Projects must configure this file during `/devflow-setup`**

Execute the command `/check` based on content of `$ARGUMENTS` and strictly follow this process.

---
name: devflow-dev
description: Implement features from GitHub issues with complete development workflow including branch creation, implementation, validation, and PR generation. Use when users want to implement an issue or develop a feature. Trigger phrases: "implement issue", "develop feature", "code feature", "/dev", "start development"
type: flow
---

# DevFlow: Development Implementation Flow

Implement features based on GitHub issues, creating a development branch, following best practices, and ending with Pull Request generation.

## When to Use

Use this flow when you need to:
- Implement a feature from a GitHub issue
- Develop code following structured workflow
- Create a pull request from an issue
- Follow project conventions and best practices

## Flow Diagram

```mermaid
flowchart TD
    A([BEGIN]) --> B[Download and parse GitHub issue]
    B --> C{Uncommitted changes?}
    C -->|Yes| D[Ask user: stash/commit/discard]
    D --> E
    C -->|No| E[Analyze issue specification]
    E --> F[Create feature branch]
    F --> G[Prepare workspace and dependencies]
    G --> H[Run initial validation]
    H --> I[Extract task checklist from issue]
    I --> J{All tasks complete?}
    J -->|No| K[Implement next task]
    K --> L[Run tests for changes]
    L --> M[Commit with descriptive message]
    M --> J
    J -->|Yes| N[Run full validation suite]
    N --> O{Validation passed?}
    O -->|No| P[Fix issues found]
    P --> N
    O -->|Yes| Q[Generate PR description]
    Q --> R[Create Pull Request]
    R --> S([END: Next use /flow:devflow-review-pr])
```

## Node Details

### 1. Download Issue
Fetch complete issue information from GitHub including:
- Title and description
- Acceptance criteria
- Labels and assignees
- Comments and discussion

### 2. Check Git State
Ensure clean working directory before starting.

### 3. Create Branch
Create properly named branch:
- Format: `feat/issue-<number>-<slug>`
- Based on: `main` or epic branch if applicable

### 4. Prepare Workspace
- Install/update dependencies
- Run initial validation
- Ensure clean starting point

### 5. Implementation Loop
Process each task from the issue checklist:
- Implement one task at a time
- Run relevant tests
- Make frequent commits
- Validate no regressions

### 6. Final Validation
Run complete validation suite:
- All tests
- Linting
- Type checking
- Build verification

### 7. Create PR
Generate comprehensive PR with:
- Link to issue
- Summary of changes
- Testing performed
- Acceptance criteria verification

## Parameters

The flow accepts these arguments:
- `issue#<number>`: Required - the issue to implement
- `--branch=<name>`: Optional custom branch name
- `--draft`: Create PR as draft
- `--auto-tests`: Run tests after each change

## Example Usage

```
/flow:devflow-dev issue#123
/flow:devflow-dev issue#456 --draft
/flow:devflow-dev issue#789 --auto-tests
```

## Output

After completion:
- Feature implemented on branch
- All tests passing
- Pull Request created
- Clear next step: `/flow:devflow-review-pr <pr-number>`

---
name: devflow-review-pr
description: Perform complete technical review of Pull Requests including branch checkout, validation, and approval. Use when users want to review a PR or verify changes. Trigger phrases: "review PR", "check pull request", "approve PR", "/review-pr", "validate PR"
type: flow
---

# DevFlow: Pull Request Review Flow

Perform complete technical review of Pull Requests, including branch checkout, technical validation, error correction, and quality approval.

## When to Use

Use this flow when you need to:
- Review a pull request technically
- Validate PR quality before merge
- Check out and test PR changes
- Approve or request changes on PR

## Flow Diagram

```mermaid
flowchart TD
    A([BEGIN]) --> B[Fetch PR info from GitHub]
    B --> C[Identify linked issue]
    C --> D[Analyze modified files]
    D --> E[Checkout PR branch]
    E --> F[Install dependencies if needed]
    F --> G[Run technical validations]
    G --> H{Validation passed?}
    H -->|No| I{Auto-fix enabled?}
    I -->|Yes| J[Auto-correct issues]
    J --> G
    I -->|No| K[Report issues to user]
    K --> L[User decides action]
    H -->|Yes| L
    L --> M{Functional tests configured?}
    M -->|Yes| N[Start local server]
    N --> O[Run functional tests]
    O --> P[Capture evidence]
    M -->|No| Q[Skip functional tests]
    P --> R[Consolidate results]
    Q --> R
    R --> S[Classify findings by severity]
    S --> T{Auto-approve & no critical issues?}
    T -->|Yes| U[Auto-approve PR]
    T -->|No| V[Present review to user]
    V --> W{User decision?}
    W -->|Approve| X[Approve PR]
    W -->|Comment| Y[Add review comments]
    W -->|Request changes| Z[List required changes]
    U --> AA([END])
    X --> AA
    Y --> AA
    Z --> AA
```

## Node Details

### 1. PR Analysis
- Fetch PR details from GitHub
- Identify linked issue for context
- Analyze changed files and impact

### 2. Environment Setup
- Checkout PR branch (handle forks)
- Install/update dependencies
- Ensure clean test environment

### 3. Technical Validation
Run complete validation suite:
- Tests
- Linting
- Type checking
- Build

### 4. Auto-Fix (Optional)
If `--fix-issues` flag and validation fails:
- Attempt automatic corrections
- Re-run validations
- Report what was fixed

### 5. Functional Testing (Optional)
If configured in `.claude/details/commands/review-pr.md`:
- Start local server
- Run automated functional tests
- Capture screenshots/logs as evidence

### 6. Review Decision
Based on findings, either:
- Auto-approve (if enabled and clean)
- Present findings to user for decision
- Provide approve/comment/request-changes options

## Parameters

- `<pr-number>`: Required - PR to review
- `--fix-issues`: Automatically correct found problems
- `--auto-approve`: Auto-approve if no critical issues
- `--functional-tests`: Enable functional testing

## Example Usage

```
/flow:devflow-review-pr 123
/flow:devflow-review-pr 456 --fix-issues
/flow:devflow-review-pr 789 --auto-approve
```

## Output

Complete review report:
```
📋 COMPLETE REVIEW - PR #123

🔗 Implemented issue: #456 ✅
🔧 Technical validations: ✅ 4/4 passing
📊 Coverage: 94% (+2% vs baseline)
🧪 Functional tests: ✅ All passed

✅ Ready for merge
```

---
description: "Implement features based on GitHub issues, creating development branch, following best practices, and generating complete Pull Request"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - Task
  - TodoWrite
argument-hints:
  - "issue#<number>"
  - "--branch=custom-name"
  - "--draft"
  - "--auto-tests"
  - "--full-validation"
---

# Development Implementation Command

Command to implement features based on GitHub issues, creating a development branch, following project best practices, and ending with Pull Request generation.

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`
- Remote URL: !`git remote get-url origin`

## Usage

```bash
/dev issue#<number> [--branch=custom-name] [--draft] [--auto-tests] [--full-validation]
```

## Objective

Implement complete features based on existing GitHub issues, following a structured development flow that includes:
- Issue specification download and analysis
- Development branch creation
- Step-by-step implementation following best practices
- Continuous validation with tests and linting
- Pull Request generation with complete documentation

## Parameters

- `issue#<number>`: Issue number to implement (required)
- `--branch`: Custom name for the branch (optional, auto-generates by default)
- `--draft`: Create PR as draft for incremental review (optional)
- `--auto-tests`: Automatically run tests after each change (optional)
- `--full-validation`: Run complete validation suite at the end (optional)

## Instructions for Claude

**IMPORTANT - Complete and structured development flow**

### Implementation Flow

The command has automatic access to git context (see Context section above).

1. **State Verification**: Review git context to detect uncommitted changes
2. **Issue Download**: Get all issue information from GitHub
3. **Specification Analysis**: Parse and structure technical specification
4. **Environment Preparation**: Create branch and configure development workspace
5. **Guided Implementation**: Develop step by step following issue checklist
6. **Continuous Validation**: Run tests and validations during development
7. **Finalization**: Create Pull Request with complete documentation

### Detailed Process

#### 1. Issue Download and Analysis

**Getting Information**
```bash
# Download complete issue information
gh issue view <number> --json title,body,assignees,labels,milestone,state,comments

# Verify issue is open and assigned
# Extract technical specification and task checklist
# Identify affected areas and dependencies
```

**Issue Validation**
- Verify issue exists and is accessible
- Confirm it has complete technical specification
- Validate it includes clear acceptance criteria
- Verify it has implementation checklist

#### 2. Development Environment Preparation

**Git State Verification**

Git context is already automatically available. If there are uncommitted changes (detected in `git status`), ask user what to do:
- **Stash**: `git stash save "WIP before /dev issue#X"`
- **Commit**: Create commit with current changes
- **Discard**: `git reset --hard` (with confirmation)

**Branch Creation**
```bash
# Determine branch name based on issue
BRANCH_NAME="feat/issue-<number>-<title-slug>"

# Ensure we're on main branch updated
git checkout main
git pull origin main

# Create new branch for development
git checkout -b $BRANCH_NAME
git push -u origin $BRANCH_NAME
```

**Epic Integration**
If the issue is part of an epic:
```bash
# Check issue labels/body for epic reference
# If part of epic, base branch should be epic branch
EPIC_BRANCH="epic/<epic-name>"
git checkout $EPIC_BRANCH
git pull origin $EPIC_BRANCH
git checkout -b $BRANCH_NAME
git push -u origin $BRANCH_NAME
```

**Workspace Configuration**

Read from `.claude/details/commands/dev.md` for project-specific setup:
```bash
# Example for Node.js projects:
npm ci
# Generate types if necessary
# Verify environment is clean
```

**Initial Validation**
```bash
# Run quick validation to ensure clean starting point
/check --fast
```

#### 3. Step-by-Step Implementation

**Specification Analysis**
- Extract task checklist from issue
- Prioritize tasks by dependencies
- Identify optimal implementation order
- Plan intermediate validations

**Incremental Development**
- Implement one task at a time from checklist
- Run relevant tests after each change
- Make frequent commits with descriptive messages
- Validate each step doesn't break existing functionality

**Implementation Patterns**
- Follow existing project conventions
- Use established libraries and utilities
- Respect project architecture
- Implement appropriate error handling
- Consider security and performance aspects

#### 4. Continuous Validation

**Tests During Development**

Read from `.claude/details/commands/dev.md` for project-specific test commands:
```bash
# Example commands (project-specific):
npm run test
# or
pytest tests/
# or
./gradlew test

# Quick validation during development
/check --fast

# Complete validation at key points
/check
```

**Acceptance Criteria Validation**
- Verify each acceptance criterion from issue
- Test edge cases and error handling
- Validate integration with other components
- Confirm no regressions introduced

#### 5. Finalization and Pull Request

**Final Validation**
```bash
# Complete validation suite using optimized command
/check --fast    # For quick validation (without build)
/check          # For complete validation including build

# Verify test coverage if necessary
# (project-specific command from details file)
```

**Pull Request Preparation**
- Generate description based on implemented issue
- Include summary of changes made
- Document testing strategy used
- Create review checklist

**Creating Pull Request**

Determine base branch:
- If part of epic: base = epic branch
- Otherwise: base = main

```bash
gh pr create \
  --title "feat: [Title based on issue]" \
  --body "$(cat <<'EOF'
## 🔗 Related Issue
Closes #<number>

## 📋 Changes Summary
[Description of implemented changes]

## ✅ Completed Acceptance Criteria
[List of verified criteria from issue]

## 🧪 Testing
[Description of testing performed]

## 📝 Notes for Reviewers
[Important information for review]

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)" \
  --base <base-branch> \
  --head $BRANCH_NAME
```

### Technical Considerations

#### Project Compatibility
- Identify affected areas automatically
- Run specific commands per area when necessary
- Verify interdependencies
- Validate changes don't affect other areas

#### Best Practices Adherence
- Frequent commits with descriptive messages following conventions
- Incremental implementation following issue checklist
- Continuous validation to avoid regressions
- Documentation of complex changes

#### Error Handling and Contingencies
- Automatic rollback if validations fail
- Checkpoint commits for recovery
- Documentation of problems found during implementation
- Escalation to user when decisions needed

### Integration with Other Commands

#### Complete Development Flow
1. `/feat` → Create technical specification and issue
2. `/dev issue#X` → Implement functionality (uses `/check` for validations)
3. `/check` → Validate implementation quality
4. `/review-pr pr#Y` → Review and approve Pull Request

#### Handoff Between Commands
- `/dev` uses specification generated by `/feat`
- `/review-pr` can reference original issue for context
- Shared information through GitHub metadata

### Common Use Cases

#### Complete Feature Implementation
```bash
/dev issue#123
# Implements full issue functionality following specification
```

#### Development with Continuous Validation
```bash
/dev issue#123 --auto-tests
# Automatically runs tests after each significant change
```

#### Incremental Development with Draft PR
```bash
/dev issue#123 --draft
# Creates PR as draft for incremental progress review
```

#### Exhaustive Validation
```bash
/dev issue#123 --full-validation
# Runs all possible validations at the end
```

### User Output

**Process Start**
```
🚀 STARTING DEVELOPMENT - Issue #<number>

📋 Issue: [Issue Title]
🎯 Objective: [Issue Summary]
🏗️ Affected areas: [List of areas]

📝 Loaded specification:
- Acceptance criteria: [X] items
- Implementation tasks: [Y] items
- Testing strategy: [Description]

🌿 Creating branch: feat/issue-<number>-<slug>

Proceed with implementation? (Y/n)
```

**During Development**
```
🔧 Implementing: [Task Name]
✅ Tests passing: [X/Y]
📊 Progress: [X/Y] tasks completed
⏱️ Estimated remaining time: [estimate]
```

**Finalization**
```
✅ IMPLEMENTATION COMPLETED - Issue #<number>

📊 Summary:
- Modified files: [quantity]
- Tests added/modified: [quantity]
- Commits made: [quantity]
- Acceptance criteria met: [X/Y]

🔍 Final validations (/check):
- ✅ Linting: No errors
- ✅ Type checking: No errors
- ✅ Tests: [X] passing, [Y] added
- ✅ Build: Successful
- ⏱️ Total time: [X]s (parallel)

🚀 Pull Request created: #<pr-number>
📋 Issue will close automatically on merge

🎯 Next step: /review-pr <pr-number> for technical review
```

## Project Customization

**IMPORTANT**: Each project must customize development details in:
`.claude/details/commands/dev.md`

This file should include:
- Dependency installation commands
- Project-specific test commands
- Build and validation commands
- Environment setup procedures
- Framework-specific considerations
- Code organization patterns

**Projects must configure this file during `/devflow-setup`**

## Reference

For specific procedures, troubleshooting, and advanced configurations, consult:
`.claude/details/commands/dev.md`

---
description: "Generate detailed technical specifications and create GitHub issues with acceptance criteria, impact analysis, and all necessary information for implementation"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Bash(git status:*)
  - Bash(git diff:*)
  - Bash(git branch:*)
  - Bash(git log:*)
  - Bash(git remote:*)
  - Bash(gh label:*)
  - Bash(gh issue:*)
  - WebSearch
  - Task
argument-hints:
  - "<feature-name>"
  - "--type=feat"
  - "--type=fix"
  - "--type=docs"
  - "--type=refactor"
  - "--type=test"
  - "--type=chore"
  - "--priority=low"
  - "--priority=medium"
  - "--priority=high"
  - "--priority=critical"
---

# Feature Specification & Issue Generation Command

Command to generate detailed technical specifications for features and create GitHub issues with all necessary information for implementation.

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`
- Remote URL: !`git remote get-url origin`
- GitHub labels: !`gh label list --json name,description,color`

## Usage

```bash
/feat <feature-name> [--type=feat|fix|docs|refactor|test|chore] [--priority=low|medium|high|critical]
```

## Objective

Generate complete technical specifications and create GitHub issues with detailed acceptance criteria, impact analysis, and all information necessary for any developer to implement the feature following project best practices.

## Parameters

- `<feature-name>`: Name of the feature in kebab-case
- `--type`: Type of change (default: `feat`)
  - `feat`: New feature
  - `fix`: Bug fix
  - `docs`: Documentation
  - `refactor`: Code refactoring
  - `test`: Tests
  - `chore`: Maintenance tasks
- `--priority`: Issue priority (default: `medium`)

## Instructions for Claude

**IMPORTANT - Do not create pending tasks at command start**

### Natural Interaction Flow

1. **Immediately**: Ask user for high-level description of the feature
   - Example: "Describe the feature you want to implement in the project"
   - DO NOT create a structured list of questions at the start

2. **Description analysis**: Based on user input, automatically infer and complete as much information as possible

3. **Specific questions**: Only ask additional questions if there are critical aspects that cannot be inferred:
   - Project scope (if not clear)
   - Database impact (if relevant)
   - Special considerations
   - Non-obvious critical dependencies

Based on user description and project knowledge, complete:
- **Motivation and problem**: Infer from context
- **Affected components**: Analyze based on current architecture
- **Acceptance criteria**: Generate based on best practices
- **Testing strategy**: Define according to project patterns
- **Affected areas**: Determine based on change nature

### Command Flow

The command has automatic access to git context and GitHub labels (see Context section above).

1. **Immediately**: Request high-level feature description
2. **Intelligent analysis**: Automatically infer maximum information using available context
3. **Specific questions**: Only if absolutely necessary for critical aspects
4. **Load details**: Read `.claude/details/commands/feat.md` for complete process and templates
5. **Verify connectivity**: With GitHub in background
6. **Analyze codebase**: Review existing architecture and project patterns
7. **Generate specification**: Create complete technical specification using detailed templates
8. **Mandatory review**: Present specification to user for approval
9. **Label management**: Verify and create needed labels before creating issue (using context list)
10. **Create issue**: Only after user approval and with appropriate labels
11. **Flow information**: Inform user about next step with `/dev issue#X`

### Details File Usage

**IMPORTANT!** For complete specification and issue generation process, Claude MUST read and follow detailed instructions in:

**`.claude/details/commands/feat.md`**

This file contains:
- Complete issue template
- Validation checklist
- Specific technical commands
- Troubleshooting procedures
- Anti-patterns to avoid
- Detailed best practices

### Label/Tag Management

**Before creating the issue**, verify and manage labels:

1. **List existing labels**:
   ```bash
   gh label list --json name,description,color
   ```

2. **Identify needed labels** based on issue type:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation
   - `refactor`: Refactoring
   - `test`: Tests
   - `chore`: Maintenance tasks
   - Priority labels: `priority:low`, `priority:medium`, `priority:high`, `priority:critical`
   - Component labels: Based on affected areas

3. **Create missing labels** if they don't exist:
   ```bash
   gh label create "label-name" --description "Description" --color "HEXCOLOR"
   ```

4. **Apply labels to issue** during creation:
   ```bash
   gh issue create ... --label "feat,priority:medium,component-name"
   ```

### Issue Template Structure

The generated issue should include:

```markdown
## Description

<Clear description of the feature/fix>

## Motivation

<Why is this needed? What problem does it solve?>

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Technical Approach

<High-level technical approach>

## Affected Components

- Component 1: <description of changes>
- Component 2: <description of changes>

## Implementation Checklist

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Testing Strategy

<How should this be tested?>

## Dependencies

<Any dependencies or prerequisites>

## Considerations

<Security, performance, accessibility, etc.>

## Definition of Done

- [ ] Implementation complete
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] All acceptance criteria met

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### Technical Considerations

- **Git Context**: Obtain repository information at start for complete context
- **Automatic Labels**: Verify and create necessary labels before creating issue
- **Specification Only**: This command does NOT implement code, only generates technical specification
- **Codebase Analysis**: Examine existing code for technical context, not to modify it
- **Complete Specification**: Must include all information necessary for implementation
- **Mandatory Review**: User MUST review and approve specification before creating issue

### Integration with Development Flow

This command is part of a complete development flow:

**Complete Flow**: `/feat` → `/dev` → `/check` → `/review-pr`

1. **`/feat`** (this command): Generate complete technical specification and GitHub issue
2. **`/dev issue#X`**: Implement functionality following issue specification
3. **`/check`**: Execute project validations (tests, linting, etc.)
4. **`/review-pr pr#Y`**: Technically review generated Pull Request

**Output to User After Creating Issue**:
```
✅ Issue #123 created successfully: "Feature Title"
🔗 URL: https://github.com/repo/issues/123

🚀 Next step for implementation:
   /dev issue#123

💡 The issue contains all necessary information for implementation
```

### Epic Integration

If this feature is part of an epic:

```bash
# Reference the epic in the issue
/feat <feature-name> --epic=<epic-number>

# The issue will automatically:
# - Link to the epic issue
# - Use epic branch as base branch
# - Include epic context in description
```

### Customization

For project-specific templates and processes:
`.claude/details/commands/feat.md`

This file should include:
- Project-specific issue template
- Required sections and format
- Technical validation checklist
- Framework-specific considerations
- Team conventions
- Compliance requirements

**Projects must customize this file during `/devflow-setup`**

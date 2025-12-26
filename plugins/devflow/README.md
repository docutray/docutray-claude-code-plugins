# DevFlow Commands

A comprehensive set of slash commands for Claude Code that implement a complete agile development workflow based on GitHub and best practices.

## Overview

DevFlow provides a structured approach to software development, from research and planning through implementation and review. All commands are framework-agnostic and can be customized for your project's specific needs.

## Commands

### Core Workflow Commands

#### `/devflow:feat` - Feature Specification
Create detailed technical specifications and GitHub issues with acceptance criteria.

```bash
/devflow:feat <feature-name> [--type=feat|fix|docs|refactor|test|chore] [--priority=low|medium|high|critical]
```

**When to use**: When you have a clear feature or fix to implement.

#### `/devflow:dev` - Development Implementation
Implement features based on GitHub issues, following best practices and ending with a Pull Request.

```bash
/devflow:dev issue#<number> [--branch=custom-name] [--draft] [--auto-tests] [--full-validation]
```

**When to use**: After creating an issue with `/devflow:feat` and ready to implement.

#### `/devflow:check` - Quality Validation
Execute all project validations in parallel: tests, linting, type checking, and build.

```bash
/devflow:check              # All validations
/devflow:check --fast       # Skip build
/devflow:check --verbose    # Show full output
```

**When to use**: During development to validate changes, or as part of PR review.

#### `/devflow:review-pr` - Pull Request Review
Perform complete technical review of Pull Requests with optional functional testing.

```bash
/devflow:review-pr <pr-number> [--fix-issues] [--auto-approve] [--functional-tests]
```

**When to use**: After a PR is created to review and approve changes.

### Optional Planning Commands

#### `/devflow:research` - Research & Analysis
Research topics and technologies before creating epics or features.

```bash
/devflow:research <topic> [--depth=shallow|medium|deep] [--output=summary|detailed|report]
```

**When to use**: Before starting major initiatives or when evaluating technologies.

#### `/devflow:epic` - Epic Planning
Create epic issues for major initiatives with multiple phases and related issues.

```bash
/devflow:epic <epic-name> [--priority=low|medium|high|critical] [--target-version=X.Y.Z]
```

**When to use**: For large features that span multiple issues and require dedicated planning.

### Setup Command

#### `/devflow:devflow-setup` - Configuration
Configure DevFlow commands for your project's framework and requirements.

```bash
/devflow:devflow-setup [--framework=<name>] [--force]
```

**When to use**: First time using DevFlow in a project, or when reconfiguring.

## Development Flows

### Standard Flow (Recommended)

For most features and fixes:

```
/devflow:feat → /devflow:dev → /devflow:check → /devflow:review-pr
```

1. **`/devflow:feat new-feature`** - Create feature specification and GitHub issue
2. **`/devflow:dev issue#123`** - Implement the feature
  - If OpenSpec is enabled in the repo, `/devflow:dev` generates an OpenSpec proposal from the issue at the start of the work.
3. **`/devflow:check`** - Validate implementation
  - If OpenSpec is enabled, `/devflow:check` can also archive the proposal as a pre-PR gate.
4. **`/devflow:review-pr 45`** - Review and approve PR

### OpenSpec-Enhanced Flow

If your team uses OpenSpec for design proposals, DevFlow can incorporate it as part of the normal flow:

```
/devflow:feat → /devflow:dev (generate proposal) → /devflow:check (archive proposal) → /devflow:review-pr
```

Key rules:
- **At dev start**: from `issue#<n>`, generate an OpenSpec proposal following your OpenSpec repo conventions.
- **Before PR**: archive the proposal and ensure the PR references the archived location.

### Epic-Based Flow

For major initiatives:

```
/devflow:research → /devflow:epic → /devflow:feat → /devflow:dev → /devflow:check → /devflow:review-pr
```

1. **`/devflow:research oauth-implementation`** - Research OAuth integration options
2. **`/devflow:epic oauth-integration`** - Create epic with multiple phases
3. **`/devflow:feat oauth-backend`** - Create spec for backend OAuth support
4. **`/devflow:dev issue#123`** - Implement OAuth backend (targets epic branch)
5. **`/devflow:check`** - Validate changes
6. **`/devflow:review-pr 45`** - Review PR (merges to epic branch)
7. Repeat steps 3-6 for other epic components
8. Create final PR from epic branch to main

### Quick Fix Flow

For simple fixes:

```
/devflow:feat → /devflow:dev → /devflow:review-pr
```

Skip `/devflow:check` as it's automatically run by `/devflow:dev` and `/devflow:review-pr`.

## Getting Started

### 1. Install DevFlow Commands

**Step 1: Add the marketplace**
```bash
/plugin marketplace add docutray/docutray-claude-code-plugins
```

**Step 2: Install the plugin**
```bash
/plugin install devflow@docutray-plugins
```

**Or use the interactive menu:**
```bash
/plugin
# Select "Browse Plugins" and choose devflow
```

This gives you:
- ✅ Latest version from GitHub
- ✅ Easy updates with reinstall
- ✅ Access to all 7 DevFlow commands

**For local development:**
```bash
git clone https://github.com/docutray/docutray-claude-code-plugins
cd docutray-claude-code-plugins
/plugin marketplace add .
/plugin install devflow@local
```

### 2. Configure for Your Project

Run the setup command in your project:

```bash
/devflow:devflow-setup
```

This will:
- Detect your project's framework
- Ask configuration questions
- Generate customized detail files
- Set up validation commands

### 3. Start Using the Flow

Create your first feature:

```bash
/devflow:feat user-authentication --type=feat --priority=high
```

## Configuration

### Project-Specific Configuration

After running `/devflow-setup`, configuration files are created in:

```
.claude/details/commands/
├── check.md          # Validation commands
├── feat.md           # Issue template
├── dev.md            # Development workflow
└── review-pr.md      # Review criteria
```

### Customizing Commands

Edit these files to customize for your project:

**`check.md`** - Define validation commands:
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

**`dev.md`** - Define development setup:
- Dependency installation
- Environment setup
- Development server commands
- Testing procedures

### OpenSpec

If your repo uses OpenSpec, the source of truth and changes live under `openspec/`:
- `openspec/specs/` - current specs (source of truth)
- `openspec/changes/<change>/` - proposals + tasks + spec deltas

DevFlow integrates with OpenSpec by:
- generating a change proposal folder at the start of `/dev` (from the GitHub issue)
- archiving the change before opening the PR (often run as part of `/check`)

**`feat.md`** - Customize issue template:
- Required sections
- Acceptance criteria format
- Definition of done

**`review-pr.md`** - Define review criteria:
- Quality standards
- Testing requirements
- Approval criteria

## Framework Support

DevFlow includes templates for common frameworks:

- **TypeScript/Node.js** - Next.js, React, Express, etc.
- **Python** - Django, FastAPI, Flask, etc.
- **Go** - Standard Go projects
- **Ruby** - Rails, Sinatra, etc.
- **Java** - Spring, Maven/Gradle projects
- **Rust** - Cargo projects

Additional frameworks can be configured manually.

## Command Integration

### How Commands Work Together

1. **`/devflow:feat`** creates structured GitHub issues
2. **`/devflow:dev`** uses those issues to guide implementation
3. **`/devflow:check`** validates code quality (used by both `/devflow:dev` and `/devflow:review-pr`)
4. **`/devflow:review-pr`** reviews PRs created by `/devflow:dev`

### Epic Workflow

When using epics:

1. **`/devflow:epic`** creates epic issue and dedicated branch
2. **`/devflow:feat`** for epic-related features links to epic
3. **`/devflow:dev`** targets epic branch instead of main
4. **`/devflow:review-pr`** reviews PRs into epic branch
5. Final PR merges epic branch to main

### Data Flow

```
GitHub Issues ←→ /devflow:feat ←→ /devflow:dev ←→ /devflow:check
                                        ↓
                                 Pull Requests ←→ /devflow:review-pr
```

## Best Practices

### Feature Development

1. **Start small**: Break large features into smaller issues
2. **Clear criteria**: Define acceptance criteria upfront
3. **Frequent commits**: Commit often with descriptive messages
4. **Continuous validation**: Run `/devflow:check` regularly during development
5. **Complete reviews**: Use `/devflow:review-pr` for all PRs

### Epic Management

1. **Clear phases**: Break epics into logical phases
2. **Independent issues**: Each issue should be independently deliverable
3. **Dependency tracking**: Document dependencies between issues
4. **Regular sync**: Merge main into epic branch regularly
5. **Complete testing**: Test full epic before final merge

### Code Quality

1. **Run validations**: Always run `/devflow:check` before creating PR
2. **Fix issues**: Address all linting and type errors
3. **Test coverage**: Maintain minimum coverage thresholds
4. **Code review**: Use `/devflow:review-pr` for thorough reviews
5. **Documentation**: Update docs with feature changes

## Troubleshooting

### Common Issues

**Commands not working**:
- Ensure plugin is installed: `/plugin list`
- Run setup: `/devflow:devflow-setup --force`

**Validation failures**:
- Check configuration in `.claude/details/commands/check.md`
- Verify commands exist in your project
- Run commands manually to test

**GitHub integration issues**:
- Verify GitHub CLI is installed: `gh --version`
- Login to GitHub: `gh auth login`
- Check repository access

**Framework not supported**:
- Use `/devflow:devflow-setup` and select "Other"
- Manually configure validation commands
- Create templates based on examples

### Getting Help

1. Check command documentation: Read command `.md` files
2. Review configuration: Check `.claude/details/commands/`
3. Test manually: Run validation commands directly
4. Reconfigure: Use `/devflow:devflow-setup --force`

## Examples

### Example 1: Simple Feature

```bash
# Create feature specification
/devflow:feat add-dark-mode --type=feat

# Implement (creates branch, codes, creates PR)
/devflow:dev issue#123

# Review (checks out branch, validates, reviews)
/devflow:review-pr 45
```

### Example 2: Bug Fix

```bash
# Create fix specification
/devflow:feat login-redirect-bug --type=fix --priority=high

# Implement fix
/devflow:dev issue#124 --auto-tests

# Quick review and approve
/devflow:review-pr 46 --auto-approve
```

### Example 3: Large Epic

```bash
# Research first
/devflow:research microservices-architecture --depth=deep

# Create epic
/devflow:epic microservices-migration --priority=critical

# Epic creates issues #125, #126, #127, #128

# Implement first component
/devflow:dev issue#125
/devflow:review-pr 47

# Implement second component
/devflow:dev issue#126
/devflow:review-pr 48

# ... continue with remaining issues

# Finally, create PR: epic/microservices-migration → main
```

## Advanced Usage

### Custom Validations

Add project-specific validations to `check.md`:

```json
{
  "validations": {
    "security": {
      "command": "npm audit --audit-level=high",
      "description": "Security audit",
      "enabled": true
    },
    "performance": {
      "command": "npm run perf-test",
      "description": "Performance tests",
      "enabled": false
    }
  }
}
```

### Monorepo Support

Configure workspace-specific commands:

```json
{
  "validations": {
    "tests": {
      "command": "npx turbo run test",
      "description": "All workspace tests",
      "enabled": true
    }
  }
}
```

### CI/CD Integration

Align local validations with CI:

```bash
# Local validation
/devflow:check

# Should match CI validation
# .github/workflows/ci.yml
# - npm run test
# - npm run lint
# - npx tsc --noEmit
# - npm run build
```

## Contributing

To contribute to DevFlow:

1. Fork the repository
2. Create feature branch
3. Add/modify commands in `commands/`
4. Add templates in `templates/`
5. Update documentation
6. Submit pull request

## License

[Specify license]

## Support

- **Issues**: [GitHub Issues](https://github.com/docutray/docutray-claude-code-plugins/issues)
- **Documentation**: This file and command `.md` files
- **Examples**: See `templates/` directory
- **Contact**: Roberto Arce (roberto@docutray.com)

---

**Built with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) by Docutray**

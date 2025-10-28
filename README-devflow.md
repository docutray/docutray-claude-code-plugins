# DevFlow Commands

A comprehensive set of slash commands for Claude Code that implement a complete agile development workflow based on GitHub and best practices.

## Overview

DevFlow provides a structured approach to software development, from research and planning through implementation and review. All commands are framework-agnostic and can be customized for your project's specific needs.

## Commands

### Core Workflow Commands

#### `/feat` - Feature Specification
Create detailed technical specifications and GitHub issues with acceptance criteria.

```bash
/feat <feature-name> [--type=feat|fix|docs|refactor|test|chore] [--priority=low|medium|high|critical]
```

**When to use**: When you have a clear feature or fix to implement.

#### `/dev` - Development Implementation
Implement features based on GitHub issues, following best practices and ending with a Pull Request.

```bash
/dev issue#<number> [--branch=custom-name] [--draft] [--auto-tests] [--full-validation]
```

**When to use**: After creating an issue with `/feat` and ready to implement.

#### `/check` - Quality Validation
Execute all project validations in parallel: tests, linting, type checking, and build.

```bash
/check              # All validations
/check --fast       # Skip build
/check --verbose    # Show full output
```

**When to use**: During development to validate changes, or as part of PR review.

#### `/review-pr` - Pull Request Review
Perform complete technical review of Pull Requests with optional functional testing.

```bash
/review-pr <pr-number> [--fix-issues] [--auto-approve] [--functional-tests]
```

**When to use**: After a PR is created to review and approve changes.

### Optional Planning Commands

#### `/research` - Research & Analysis
Research topics and technologies before creating epics or features.

```bash
/research <topic> [--depth=shallow|medium|deep] [--output=summary|detailed|report]
```

**When to use**: Before starting major initiatives or when evaluating technologies.

#### `/epic` - Epic Planning
Create epic issues for major initiatives with multiple phases and related issues.

```bash
/epic <epic-name> [--priority=low|medium|high|critical] [--target-version=X.Y.Z]
```

**When to use**: For large features that span multiple issues and require dedicated planning.

### Setup Command

#### `/devflow-setup` - Configuration
Configure DevFlow commands for your project's framework and requirements.

```bash
/devflow-setup [--framework=<name>] [--force]
```

**When to use**: First time using DevFlow in a project, or when reconfiguring.

## Development Flows

### Standard Flow (Recommended)

For most features and fixes:

```
/feat → /dev → /check → /review-pr
```

1. **`/feat new-feature`** - Create feature specification and GitHub issue
2. **`/dev issue#123`** - Implement the feature
3. **`/check`** - Validate implementation (integrated in /dev)
4. **`/review-pr 45`** - Review and approve PR

### Epic-Based Flow

For major initiatives:

```
/research → /epic → /feat → /dev → /check → /review-pr
```

1. **`/research oauth-implementation`** - Research OAuth integration options
2. **`/epic oauth-integration`** - Create epic with multiple phases
3. **`/feat oauth-backend`** - Create spec for backend OAuth support
4. **`/dev issue#123`** - Implement OAuth backend (targets epic branch)
5. **`/check`** - Validate changes
6. **`/review-pr 45`** - Review PR (merges to epic branch)
7. Repeat steps 3-6 for other epic components
8. Create final PR from epic branch to main

### Quick Fix Flow

For simple fixes:

```
/feat → /dev → /review-pr
```

Skip `/check` as it's automatically run by `/dev` and `/review-pr`.

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
/devflow-setup
```

This will:
- Detect your project's framework
- Ask configuration questions
- Generate customized detail files
- Set up validation commands

### 3. Start Using the Flow

Create your first feature:

```bash
/feat user-authentication --type=feat --priority=high
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

1. **`/feat`** creates structured GitHub issues
2. **`/dev`** uses those issues to guide implementation
3. **`/check`** validates code quality (used by both `/dev` and `/review-pr`)
4. **`/review-pr`** reviews PRs created by `/dev`

### Epic Workflow

When using epics:

1. **`/epic`** creates epic issue and dedicated branch
2. **`/feat`** for epic-related features links to epic
3. **`/dev`** targets epic branch instead of main
4. **`/review-pr`** reviews PRs into epic branch
5. Final PR merges epic branch to main

### Data Flow

```
GitHub Issues ←→ /feat ←→ /dev ←→ /check
                          ↓
                   Pull Requests ←→ /review-pr
```

## Best Practices

### Feature Development

1. **Start small**: Break large features into smaller issues
2. **Clear criteria**: Define acceptance criteria upfront
3. **Frequent commits**: Commit often with descriptive messages
4. **Continuous validation**: Run `/check` regularly during development
5. **Complete reviews**: Use `/review-pr` for all PRs

### Epic Management

1. **Clear phases**: Break epics into logical phases
2. **Independent issues**: Each issue should be independently deliverable
3. **Dependency tracking**: Document dependencies between issues
4. **Regular sync**: Merge main into epic branch regularly
5. **Complete testing**: Test full epic before final merge

### Code Quality

1. **Run validations**: Always run `/check` before creating PR
2. **Fix issues**: Address all linting and type errors
3. **Test coverage**: Maintain minimum coverage thresholds
4. **Code review**: Use `/review-pr` for thorough reviews
5. **Documentation**: Update docs with feature changes

## Troubleshooting

### Common Issues

**Commands not working**:
- Ensure plugin is installed: `/plugin list`
- Run setup: `/devflow-setup --force`

**Validation failures**:
- Check configuration in `.claude/details/commands/check.md`
- Verify commands exist in your project
- Run commands manually to test

**GitHub integration issues**:
- Verify GitHub CLI is installed: `gh --version`
- Login to GitHub: `gh auth login`
- Check repository access

**Framework not supported**:
- Use `/devflow-setup` and select "Other"
- Manually configure validation commands
- Create templates based on examples

### Getting Help

1. Check command documentation: Read command `.md` files
2. Review configuration: Check `.claude/details/commands/`
3. Test manually: Run validation commands directly
4. Reconfigure: Use `/devflow-setup --force`

## Examples

### Example 1: Simple Feature

```bash
# Create feature specification
/feat add-dark-mode --type=feat

# Implement (creates branch, codes, creates PR)
/dev issue#123

# Review (checks out branch, validates, reviews)
/review-pr 45
```

### Example 2: Bug Fix

```bash
# Create fix specification
/feat login-redirect-bug --type=fix --priority=high

# Implement fix
/dev issue#124 --auto-tests

# Quick review and approve
/review-pr 46 --auto-approve
```

### Example 3: Large Epic

```bash
# Research first
/research microservices-architecture --depth=deep

# Create epic
/epic microservices-migration --priority=critical

# Epic creates issues #125, #126, #127, #128

# Implement first component
/dev issue#125
/review-pr 47

# Implement second component
/dev issue#126
/review-pr 48

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
/check

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

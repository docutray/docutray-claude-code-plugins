---
description: "Configure and customize devflow commands for your project's specific framework and requirements"
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
  - Task
  - AskUserQuestion
argument-hints:
  - "--framework=typescript"
  - "--framework=python"
  - "--framework=go"
  - "--framework=ruby"
  - "--framework=java"
  - "--framework=rust"
  - "--force"
---

# DevFlow Setup Command

Interactive command to configure and customize devflow commands for your project's specific framework, tech stack, and requirements.

## Usage

```bash
/devflow-setup [--framework=<name>] [--force]
```

## Objective

Guide the project through initial configuration of devflow commands, creating customized detail files that adapt the generic commands to the project's specific needs including:
- Framework-specific commands (tests, linting, build)
- Project structure and conventions
- Issue and PR templates
- Validation criteria
- Functional testing configuration (optional)
- Optional OpenSpec installation and initialization

## Parameters

- `--framework`: Pre-select framework (optional, will ask if not provided)
- `--force`: Overwrite existing configuration (optional)

## Instructions for Claude

**IMPORTANT - Interactive and intelligent configuration**

### Setup Flow

1. **Detect existing configuration**: Check if `.claude/details/commands/` already exists
2. **Project analysis**: Analyze codebase to infer framework and structure
3. **Interactive questions**: Ask user to confirm or provide missing information
4. **Optional OpenSpec setup**: Offer to install and initialize OpenSpec in the repo
5. **Template generation**: Create customized detail files
6. **Validation**: Verify generated configuration
7. **Summary**: Show created files and next steps

### Detailed Process

#### 1. Initial Detection

```bash
# Check if configuration already exists
if [ -d ".claude/details/commands" ]; then
  echo "⚠️  Existing devflow configuration found"
  if [ "$FORCE" != "true" ]; then
    echo "Use --force to overwrite"
    exit 1
  fi
fi

# Create directory structure
mkdir -p .claude/details/commands
```

#### 2. Project Analysis

**Automatic Framework Detection**:

Analyze project files to infer framework:
- `package.json` → Node.js/TypeScript (check for React, Next.js, Vue, etc.)
- `requirements.txt` or `pyproject.toml` → Python
- `go.mod` → Go
- `Gemfile` → Ruby
- `pom.xml` or `build.gradle` → Java
- `Cargo.toml` → Rust

**Analyze Project Structure**:
- Monorepo vs single project
- Test framework in use
- Linting tools configured
- Build system
- CI/CD configuration

#### 3. Interactive Configuration

**Ask User Questions** using AskUserQuestion tool:

1. **Framework Confirmation**:
```
Detected framework: <framework>
Is this correct?
- Yes, use detected framework
- No, let me specify
```

2. **Project Type**:
```
What type of project is this?
- Web application (frontend)
- API/Backend service
- Full-stack application
- Library/Package
- Mobile application
- Other
```

3. **Testing Strategy**:
```
What testing tools do you use?
[Multiple selection]
- Unit tests (Jest, pytest, etc.)
- Integration tests
- E2E tests
- No tests configured yet
```

4. **Code Quality Tools**:
```
What code quality tools are configured?
[Multiple selection]
- Linter (ESLint, flake8, etc.)
- Formatter (Prettier, Black, etc.)
- Type checker (TypeScript, mypy, etc.)
- None yet
```

5. **Build Requirements**:
```
Does your project require a build step?
- Yes, compilation required
- No, interpreted language
```

6. **Functional Testing** (Optional):
```
Do you want to enable automated functional/QA testing in PR reviews?
- Yes, configure functional tests
- No, only technical validations
- I'll configure later
```

7. **OpenSpec** (Optional):
```
Do you want to enable OpenSpec (spec-driven development) in this repo?
- Yes, install + init OpenSpec
- No
```

If enabled, ensure:
- Node.js meets OpenSpec requirement (currently Node.js >= 20.19.0)
- OpenSpec CLI is installed and the repo is initialized

#### 4. Template Generation

Based on gathered information, generate customized files:

**For `/check` - `.claude/details/commands/check.md`**:

Generate configuration based on framework:

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
      "description": "ESLint code quality",
      "enabled": true
    },
    "typecheck": {
      "command": "npx tsc --noEmit",
      "description": "TypeScript type validation",
      "enabled": true
    },
    "build": {
      "command": "npm run build",
      "description": "Project build",
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
      "description": "Pytest test suite",
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

**For `/feat` - `.claude/details/commands/feat.md`**:

Generate issue template customized for project:

```markdown
# Feature Issue Template

## Project-Specific Guidelines

### Issue Structure

<Based on project conventions>

### Required Sections

- Description
- Motivation
- Acceptance Criteria
- Technical Approach
- [Project-specific sections]

### Labeling Convention

<Project label strategy>

### Definition of Done

- [ ] Implementation complete
- [ ] Tests added (coverage > X%)
- [ ] Documentation updated
- [ ] [Project-specific criteria]

## Technical Commands

### Environment Setup
\`\`\`bash
<project-specific setup commands>
\`\`\`

### Testing
\`\`\`bash
<project-specific test commands>
\`\`\`

### Validation
\`\`\`bash
<project-specific validation commands>
\`\`\`
```

**For `/dev` - `.claude/details/commands/dev.md`**:

Generate development workflow customization:

```markdown
# Development Workflow

## Environment Setup

### Dependency Installation
\`\`\`bash
<framework-specific install command>
# Example: npm ci, pip install -r requirements.txt, go mod download
\`\`\`

### Environment Configuration
\`\`\`bash
<setup commands>
# Example: cp .env.example .env, generate types, database setup
\`\`\`

## Development Commands

### Run Development Server
\`\`\`bash
<dev server command>
# Example: npm run dev, python manage.py runserver, go run main.go
\`\`\`

### Run Tests
\`\`\`bash
<test command>
# Example: npm run test, pytest, go test ./...
\`\`\`

### Code Generation (if applicable)
\`\`\`bash
<codegen commands>
# Example: prisma generate, protoc, graphql-codegen
\`\`\`

## Project Structure

### Code Organization
<Description of project structure>

### Naming Conventions
<Project naming conventions>

### Import/Module Structure
<How imports/modules should be organized>

## Best Practices

### Commit Message Format
<Project commit convention>
Example: Conventional Commits, custom format, etc.

### Branch Naming
<Branch naming convention>
Example: feat/, fix/, refactor/, etc.

### Code Style
<Project code style guidelines>

## Testing Requirements

### Unit Tests
<Unit test requirements and examples>

### Integration Tests
<Integration test requirements if applicable>

### Test Coverage
Minimum coverage: <X%>
```

**For `/review-pr` - `.claude/details/commands/review-pr.md`**:

Generate review configuration:

```markdown
# Pull Request Review Configuration

## Technical Validation Criteria

### Code Quality
- [ ] Follows project code style
- [ ] No linting errors
- [ ] No type errors
- [ ] Proper error handling

### Testing
- [ ] Tests added for new features
- [ ] All tests passing
- [ ] Coverage maintained/improved (> X%)

### Documentation
- [ ] Code comments for complex logic
- [ ] README updated if needed
- [ ] API documentation updated (if applicable)

### Security
- [ ] No secrets in code
- [ ] Input validation implemented
- [ ] Auth/authz properly handled

## Functional Testing (Optional)

### Configuration
\`\`\`json
{
  "functional_tests": {
    "enabled": <true|false>,
    "server": {
      "command": "<dev server command>",
      "port": <port>,
      "wait_time": <milliseconds>
    },
    "test_suites": {
      "authentication": <true|false>,
      "main_flows": <true|false>,
      "critical_paths": <true|false>
    }
  }
}
\`\`\`

### Test Scenarios (if enabled)
<List of functional test scenarios>

## Approval Criteria

- [ ] All technical validations pass
- [ ] No critical or high-priority issues
- [ ] Functional tests pass (if enabled)
- [ ] Documentation complete
- [ ] Reviewer approved

## Common Issues and Solutions

<Project-specific common issues>
```

#### 5. Validation

After generating files:

```bash
# Verify all files were created
echo "🔍 Validating configuration..."

# Check each required file
for file in check.md feat.md dev.md review-pr.md; do
  if [ -f ".claude/details/commands/$file" ]; then
    echo "✅ $file created"
  else
    echo "❌ $file missing"
  fi
done

# Test a simple validation command
echo "🧪 Testing /check configuration..."
# (attempt to parse check.md config)
```

#### 6. Summary and Next Steps

**Output to User**:
```
✅ DEVFLOW SETUP COMPLETED

📋 Configuration Created:
   ✅ .claude/details/commands/check.md
   ✅ .claude/details/commands/feat.md
   ✅ .claude/details/commands/dev.md
   ✅ .claude/details/commands/review-pr.md

🎯 Framework: <detected-framework>
🧪 Tests: <configured-test-framework>
🔍 Linting: <configured-linter>
📝 Type checking: <configured-type-checker>
🏗️ Build: <configured-build-tool>

💡 Configuration Summary:

**Validation Commands (/check)**:
   • Tests: <test-command>
   • Linting: <lint-command>
   • Type checking: <typecheck-command>
   • Build: <build-command>

**Development Workflow (/dev)**:
   • Setup: <setup-commands>
   • Dev server: <dev-command>
   • Test: <test-command>

**PR Review (/review-pr)**:
   • Technical validations: Enabled
   • Functional tests: <enabled|disabled>
   • Coverage threshold: <threshold>%

🚀 Ready to Use Devflow Commands:

1. Create a feature:
   /feat new-feature-name

2. Implement it:
   /dev issue#X

3. Validate changes:
   /check

4. Review PR:
   /review-pr X

📝 You can customize these files further:
   Edit files in .claude/details/commands/ directory

💡 Tip: Run /devflow-setup --force to reconfigure
```

### Framework-Specific Templates

**Maintain templates for common frameworks** in this plugin:
`templates/<framework>/*.md`

Available templates:
- `templates/typescript-node/` - TypeScript/Node.js projects
- `templates/python/` - Python projects
- `templates/go/` - Go projects
- `templates/ruby/` - Ruby projects
- `templates/java/` - Java projects
- `templates/rust/` - Rust projects

When framework is detected/selected, copy and customize appropriate template.

### Advanced Options

**Monorepo Configuration**:
If monorepo detected (pnpm-workspace.yaml, lerna.json, etc.), ask additional questions:
- Which packages/workspaces to validate?
- Workspace-specific commands?
- Shared vs package-specific tests?

**CI/CD Integration**:
If CI config detected (.github/workflows, .gitlab-ci.yml, etc.):
- Align validation commands with CI
- Ensure local validation matches CI
- Import any custom scripts

### Re-configuration

To update existing configuration:
```bash
/devflow-setup --force

# Or manually edit files:
# .claude/details/commands/check.md
# .claude/details/commands/feat.md
# .claude/details/commands/dev.md
# .claude/details/commands/review-pr.md
```

### Troubleshooting

Common setup issues:

**Commands not found**:
- Verify commands exist in package.json / Makefile / scripts
- Update configuration with correct commands

**Wrong framework detected**:
- Use `--framework=<name>` to force framework
- Manually edit generated files

**Missing dependencies**:
- Install required dev dependencies
- Update configuration to skip unavailable validations

## Customization

After initial setup, teams can:
1. Edit generated files in `.claude/details/commands/`
2. Add project-specific sections
3. Customize templates and checklists
4. Add custom validations
5. Configure team-specific conventions

Files are designed to be maintained by the team and committed to version control.

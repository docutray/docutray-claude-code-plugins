# Docutray Claude Code Plugins

A collection of reusable plugins for [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) maintained by the Docutray organization. This repository provides custom slash commands and skills that can be installed and used across different projects.

## About Claude Code Plugins

Claude Code's plugin system extends functionality through custom commands, agents, hooks, Skills, and MCP servers that can be shared across projects and teams. Plugins organize these features in a standardized directory structure that makes them easy to discover, install, and maintain.

## Repository Structure

This repository follows the standard Claude Code plugin structure:

```
docutray-claude-code-plugins/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata and configuration
├── commands/                # Custom slash commands
│   ├── research.md          # Research command
│   ├── epic.md              # Epic planning command
│   ├── feat.md              # Feature specification command
│   ├── dev.md               # Development implementation command
│   ├── check.md             # Validation command
│   ├── review-pr.md         # PR review command
│   └── devflow-setup.md     # Setup command
├── templates/               # Framework-specific templates
│   ├── typescript-node/     # TypeScript/Node.js templates
│   └── python/              # Python templates
├── skills/                  # Agent Skills
├── README.md                # Main documentation
├── README-devflow.md        # DevFlow complete guide
└── CLAUDE.md                # Claude Code guidance
```

## Installation

### From GitHub URL (Recommended)

Install directly from the GitHub repository:

```bash
/plugin install https://github.com/docutray/docutray-claude-code-plugins
```

This method:
- ✅ Always gets the latest version
- ✅ No marketplace configuration needed
- ✅ Works in any Claude Code environment
- ✅ Automatic updates on reinstall

### From Local Development

For testing or development:

1. Clone this repository
2. Add it as a development marketplace in your Claude Code settings
3. Install via `/plugin install devflow@dev`

## Available Components

### DevFlow - Agile Development Workflow

A comprehensive set of slash commands that implement a complete agile development workflow based on GitHub and best practices.

**Quick Start**:
```bash
# Configure for your project
/devflow-setup

# Standard workflow
/feat feature-name     # Create specification
/dev issue#123        # Implement feature
/check                # Validate quality
/review-pr 45         # Review PR
```

**Commands**:
- **`/feat`** - Create detailed feature specifications and GitHub issues
- **`/dev`** - Implement features from issues with automated workflow
- **`/check`** - Run parallel validations (tests, linting, type checking, build)
- **`/review-pr`** - Perform comprehensive PR reviews
- **`/research`** - Research topics before planning (optional)
- **`/epic`** - Plan major initiatives with multiple phases (optional)
- **`/devflow-setup`** - Configure DevFlow for your project

**Framework Support**: TypeScript/Node.js, Python, Go, Ruby, Java, Rust, and more.

**[→ Read Complete DevFlow Documentation](./README-devflow.md)**

### Slash Commands

Custom slash commands are located in the `commands/` directory. Each command is a Markdown file that can include:

- Dynamic arguments using `$ARGUMENTS`, `$1`, `$2`, etc.
- Bash command execution with `!` prefix
- File references using `@` syntax
- YAML frontmatter for metadata and configuration

### Skills

Agent Skills are located in the `skills/` directory. Each skill contains a `SKILL.md` file with:

- Name and description in YAML frontmatter
- Specific trigger terms for automatic activation
- Optional tool restrictions
- Supporting documentation and resources

## Contributing

Contributions are welcome! When adding new plugins:

1. Follow the standard plugin structure
2. Include clear descriptions and documentation
3. Test thoroughly before submitting
4. Use semantic versioning in `plugin.json`

## Official Documentation

For detailed information on creating and using Claude Code plugins:

### Core Plugin Documentation
- **[Plugins Overview](https://docs.claude.com/en/docs/claude-code/plugins)** - Introduction to the plugin system, installation, and management
- **[Plugins Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)** - Detailed `plugin.json` schema and directory structure

### Component Documentation
- **[Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)** - Creating custom slash commands with arguments, bash execution, and file references
- **[Skills](https://docs.claude.com/en/docs/claude-code/skills)** - Building Agent Skills with SKILL.md files and supporting resources

### Additional Resources
- **[Claude Code Documentation Map](https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md)** - Complete documentation index
- **[Claude Code Overview](https://docs.claude.com/en/docs/claude-code/overview)** - Getting started with Claude Code

## License

[Specify your license here]

## Support

For issues or questions:
- Open an issue in this repository
- Refer to the [official Claude Code documentation](https://docs.claude.com/en/docs/claude-code/overview)
- Contact: Roberto Arce (roberto@docutray.com)

---

Built with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) by Docutray

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
├── skills/                  # Agent Skills
└── README.md
```

## Installation

### From Plugin Marketplace

If this plugin is available in a marketplace:

```bash
/plugin install docutray-plugins@marketplace-name
```

### From Local Development

For testing or development:

1. Clone this repository
2. Add it as a development marketplace in your Claude Code settings
3. Install via `/plugin install docutray-plugins@dev`

## Available Components

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
- Contact Docutray organization maintainers

---

Built with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) by Docutray

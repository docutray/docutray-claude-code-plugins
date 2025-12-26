# Docutray Plugins Marketplace

A collection of [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) plugins maintained by the Docutray organization.

## Installation

### Add the Marketplace

```bash
/plugin marketplace add docutray/docutray-claude-code-plugins
```

### Install Plugins

```bash
/plugin install <plugin-name>@docutray-plugins
```

Or use the interactive menu:
```bash
/plugin
# Select "Browse Plugins" → choose from docutray-plugins
```

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| [devflow](./plugins/devflow/) | Complete agile development workflow with GitHub integration | 1.1.1 |

## Plugin: DevFlow

A comprehensive set of slash commands that implement a complete agile development workflow based on GitHub and best practices.

### Quick Start

```bash
# Install
/plugin install devflow@docutray-plugins

# Configure for your project
/devflow-setup

# Standard workflow
/feat feature-name     # Create specification & GitHub issue
/dev issue#123         # Implement feature
/check                 # Validate quality
/review-pr 45          # Review PR
```

### Commands

| Command | Description |
|---------|-------------|
| `/devflow-setup` | Configure DevFlow for your project |
| `/feat` | Create feature specifications and GitHub issues |
| `/dev` | Implement features from GitHub issues |
| `/check` | Run parallel validations (tests, lint, types, build) |
| `/review-pr` | Perform comprehensive PR reviews |
| `/research` | Research topics before planning |
| `/epic` | Plan major initiatives with multiple phases |

### Framework Support

TypeScript/Node.js, Python, Go, Ruby, Java, Rust, and more.

[**View Full Documentation**](./plugins/devflow/README.md)

## Repository Structure

```
docutray-claude-code-plugins/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace catalog
├── plugins/
│   └── devflow/              # DevFlow plugin
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/
│       ├── templates/
│       └── README.md
├── README.md                 # This file
└── CLAUDE.md
```

## Local Development

```bash
# Clone the repository
git clone https://github.com/docutray/docutray-claude-code-plugins
cd docutray-claude-code-plugins

# Add as local marketplace
/plugin marketplace add .

# Install plugins
/plugin install devflow@docutray-plugins
```

## Adding New Plugins

1. Create a new directory under `plugins/`:
   ```
   plugins/new-plugin/
   ├── .claude-plugin/
   │   └── plugin.json
   ├── commands/
   └── README.md
   ```

2. Add the plugin to `marketplace.json`:
   ```json
   {
     "plugins": [
       { "name": "new-plugin", "source": "new-plugin", ... }
     ]
   }
   ```

3. Document the plugin in its own `README.md`

## Official Documentation

- [Plugins Overview](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugins Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- [Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- [Skills](https://docs.claude.com/en/docs/claude-code/skills)

## License

MIT

## Support

- **Issues**: [GitHub Issues](https://github.com/docutray/docutray-claude-code-plugins/issues)
- **Contact**: Roberto Arce (roberto@docutray.com)

---

Built with [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) by Docutray

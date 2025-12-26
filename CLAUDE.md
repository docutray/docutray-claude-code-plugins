# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Claude Code plugin marketplace** for the Docutray organization. It contains multiple reusable plugins with slash commands and skills that can be installed across different projects. This is NOT an application codebase - it's a collection of plugin components organized as a marketplace.

## Repository Structure

```
docutray-claude-code-plugins/
├── .claude-plugin/
│   └── marketplace.json      # Central marketplace catalog
├── plugins/
│   └── <plugin-name>/        # Each plugin in its own directory
│       ├── .claude-plugin/
│       │   └── plugin.json   # Plugin manifest
│       ├── commands/         # Slash commands
│       ├── skills/           # Agent skills (optional)
│       ├── templates/        # Supporting files (optional)
│       └── README.md         # Plugin documentation
├── README.md                 # Marketplace documentation
└── CLAUDE.md                 # This file
```

## Plugin Architecture

### Marketplace (Root Level)

- **`.claude-plugin/marketplace.json`**: Central catalog listing all available plugins
- Uses `metadata.pluginRoot: "./plugins"` to simplify source paths
- Each plugin entry references its directory name under `plugins/`

### Individual Plugins

Each plugin follows the standard Claude Code plugin structure:

- **`.claude-plugin/plugin.json`**: Plugin manifest with metadata and versioning
- **`commands/`**: Markdown files defining slash commands with YAML frontmatter
- **`skills/`**: Agent Skills in subdirectories with `SKILL.md` files
- **`README.md`**: Plugin-specific documentation

### Key Concepts

**Slash Commands vs Skills:**
- **Commands**: User-invoked via `/command-name`, defined in `.md` files, support arguments (`$ARGUMENTS`, `$1`, `$2`), bash execution (`!`), and file references (`@`)
- **Skills**: Auto-activated by Claude based on context, defined in `SKILL.md` files, require specific trigger terms in descriptions for proper activation

**Plugin Distribution:**
- Users add the marketplace: `/plugin marketplace add docutray/docutray-claude-code-plugins`
- Users install plugins: `/plugin install <plugin-name>@docutray-plugins`
- Semantic versioning in each plugin's `plugin.json` is required

## Working with This Repository

### Adding a New Plugin

1. Create plugin directory: `plugins/<plugin-name>/`
2. Create manifest: `plugins/<plugin-name>/.claude-plugin/plugin.json`
3. Add commands in `plugins/<plugin-name>/commands/`
4. Add skills in `plugins/<plugin-name>/skills/` (optional)
5. Create `plugins/<plugin-name>/README.md`
6. Register in `.claude-plugin/marketplace.json`:
   ```json
   {
     "plugins": [
       {
         "name": "<plugin-name>",
         "source": "<plugin-name>",
         "description": "...",
         "version": "1.0.0"
       }
     ]
   }
   ```

### Adding a Slash Command to Existing Plugin

1. Create `.md` file in `plugins/<plugin-name>/commands/`
2. Add YAML frontmatter (description, allowed-tools, argument-hint)
3. Write the command prompt content
4. Update plugin version in `plugin.json`

### Adding a Skill to Existing Plugin

1. Create directory: `plugins/<plugin-name>/skills/<skill-name>/`
2. Create `SKILL.md` with required frontmatter:
   - `name`: lowercase with hyphens (max 64 chars)
   - `description`: must include trigger terms (max 1024 chars)
3. Add supporting files if needed
4. Update plugin version in `plugin.json`

## Development Workflow

1. Add or modify plugin files
2. Update plugin's `plugin.json` version
3. Update `marketplace.json` version if needed
4. Test locally:
   ```bash
   /plugin marketplace add .
   /plugin install <plugin-name>@docutray-plugins
   ```
5. Uninstall and reinstall to verify changes

Use `claude --debug` to troubleshoot plugin loading issues.

## Current Plugins

| Plugin | Description |
|--------|-------------|
| `devflow` | Complete agile development workflow with GitHub integration |

## Official References

- [Plugins Overview](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugins Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- [Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- [Skills](https://docs.claude.com/en/docs/claude-code/skills)

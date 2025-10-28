# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Claude Code plugin repository** for the Docutray organization. It contains reusable slash commands and skills that can be installed across different projects. This is NOT an application codebase - it's a collection of plugin components.

## Plugin Architecture

Claude Code plugins follow a standardized structure:

- **`.claude-plugin/plugin.json`**: Required manifest file with plugin metadata, versioning, and component path configuration
- **`commands/`**: Markdown files defining custom slash commands with optional YAML frontmatter
- **`skills/`**: Agent Skills, each in their own directory containing a `SKILL.md` file with YAML frontmatter

### Key Concepts

**Slash Commands vs Skills:**
- **Commands**: User-invoked via `/command-name`, defined in `.md` files, support arguments (`$ARGUMENTS`, `$1`, `$2`), bash execution (`!`), and file references (`@`)
- **Skills**: Auto-activated by Claude based on context, defined in `SKILL.md` files, require specific trigger terms in descriptions for proper activation

**Plugin Distribution:**
- Plugins are installed via plugin marketplaces using `/plugin install docutray-plugins@marketplace-name`
- Local development uses development marketplace structure
- Semantic versioning in `plugin.json` is required for proper version management

## Working with This Repository

### Adding a New Slash Command

1. Create a new `.md` file in `commands/` directory
2. Add YAML frontmatter if needed (description, allowed-tools, model)
3. Write the command prompt content
4. Test by installing plugin locally

### Adding a New Skill

1. Create a new directory in `skills/` (e.g., `skills/my-skill/`)
2. Create `SKILL.md` with required frontmatter:
   - `name`: lowercase with hyphens (max 64 chars)
   - `description`: must include specific trigger terms (max 1024 chars)
3. Add supporting files in the same directory if needed
4. Test that Claude auto-activates the skill based on trigger terms

### Plugin Manifest Requirements

The `plugin.json` must specify:
- `name`: Unique identifier in kebab-case
- `version`: Semantic versioning format
- Component paths (commands, agents, skills, hooks, mcpServers) if using non-default locations

All custom paths must be relative to plugin root and start with `./`

## Development Workflow

Since this repository currently has no build system, linting, or testing infrastructure, development is file-based:

1. Add or modify command/skill files
2. Update `plugin.json` version if publishing changes
3. Test by installing the plugin in a development marketplace
4. Uninstall and reinstall to verify changes load correctly

Use `claude --debug` to troubleshoot plugin loading issues.

## Official References

Key documentation for working with plugins:
- [Plugins Overview](https://docs.claude.com/en/docs/claude-code/plugins)
- [Plugins Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference) - `plugin.json` schema
- [Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- [Skills](https://docs.claude.com/en/docs/claude-code/skills)

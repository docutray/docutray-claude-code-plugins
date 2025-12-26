# Changelog

All notable changes to this project are documented in this file.

This project follows Semantic Versioning.

## [1.1.1] - 2025-12-26

### Fixed
- Fix marketplace source path to use `./` prefix (required by schema)

## [1.1.0] - 2025-12-26

### Changed
- **BREAKING**: Reorganized repository to marketplace structure for multiple plugins
- Moved devflow plugin to `plugins/devflow/` directory
- Plugin installation now uses: `/plugin install devflow@docutray-plugins`
- Moved `README-devflow.md` to `plugins/devflow/README.md`
- Updated root `README.md` as marketplace documentation
- Updated `CLAUDE.md` with new structure guidelines

### Added
- `marketplace.json` with `pluginRoot` configuration for cleaner plugin paths
- Support for multiple plugins in single repository
- Documentation for adding new plugins to the marketplace

### Removed
- Root-level `plugin.json` (now in each plugin's `.claude-plugin/` directory)
- Root-level `commands/` and `templates/` (now under `plugins/devflow/`)

## [1.0.1] - 2025-12-26

### Added
- OpenSpec integration guidance in the DevFlow docs.
- Optional OpenSpec validations (validate/archive) examples in the `/check` configuration templates.

### Changed
- `/dev` now describes generating an OpenSpec change proposal at dev start (when `openspec/` is present) and archiving the change before opening a PR.
- `/check` now documents how to wire OpenSpec validation/archive into project-specific `.claude/details/commands/check.md`.
- `/devflow-setup` now includes optional steps to install and initialize OpenSpec (`openspec init`, `openspec update`).

## [1.0.0] - 2025-12-XX

### Added
- Initial DevFlow command set: `/feat`, `/dev`, `/check`, `/review-pr`, `/research`, `/epic`, `/devflow-setup`.

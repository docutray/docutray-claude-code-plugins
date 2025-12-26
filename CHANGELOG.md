# Changelog

All notable changes to this plugin are documented in this file.

This project follows Semantic Versioning.

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

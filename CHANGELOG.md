# Changelog

All notable changes to this repository are recorded here. The version number
applies to the repository as published under `blessandy9104-hue/deepseek-agent-harness`.

The upstream DeepSeek Harness history is preserved in this repository; the
`[Upstream]` tag marks entries that originated there. This changelog starts
with the first open-source release of this repository and does not rewrite
upstream history.

## [0.1.0] — 2026-09-20

### Added

- Published the repository publicly under `blessandy9104-hue/deepseek-agent-harness`.
- Added the [Maya](python/maya/README.md) local, human-supervised Python
  assistant prototype under `python/maya/` (Apache-2.0). Maya is a standalone
  desktop assistant: chat, task tracking, supervised learning, pattern
  mapping, and safety walls. It is not part of any `dsh` profile.
- Added open-source prerequisites: `SECURITY.md`, `CODE_OF_CONDUCT.md`,
  `CHANGELOG.md`, an Apache-2.0 `LICENSE` for Maya, and a repository
  description of the projects included.
- [`Upstream`] Retains the full DeepSeek Harness codebase, documentation,
  GitHub workflows, and issue templates from the upstream project.

### Changed

- Fixed whitespace and line-ending hygiene in `python/maya/` files so the
  repository passes pre-commit whitespace checks.
- Removed a stray `_tk_diag.py` diagnostic that hard-coded a local path, and
  redacted local filesystem paths from two audit reports.
- Scoped `verify-concrete-terms` to exempt the self-contained `python/maya/`
  prototype corpus: its `provenance` identifiers predate the ban, and
  renaming its persisted JSON keys and module symbols would break runtime
  state. The exemption is recorded in the corresponding Agent Note and
  covered by the gate's spec.

### Security

- Audited all tracked files and history for credentials, private keys, API
  keys, browser data, and personal filesystem paths before publishing. No
  secrets were found.

[0.1.0]: https://github.com/blessandy9104-hue/deepseek-agent-harness/releases/tag/v0.1.0
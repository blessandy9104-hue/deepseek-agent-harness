# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| 0.1.x (`master`) | Yes |

The project is in developer preview. Only the latest commit on `master` receives security fixes; there are no long-term supported releases yet.

## Reporting a vulnerability

Do **not** open a public issue for a suspected security vulnerability. Please report it privately instead:

- Open a [private security advisory](https://github.com/blessandy9104-hue/deepseek-harness/security/advisories/new) on GitHub, or
- Report it through the upstream DeepSeek Harness project if the vulnerability affects the upstream harness code.

Please include in your report:

- The affected component or file.
- A minimal reproduction, when possible.
- Your assessment of the impact, if you have one.

You can expect an acknowledgement within 3 business days and a status update as the issue is triaged. We ask that you keep details private until a fix has been released.

## Scope

This repository combines two codebases with different licenses:

- DeepSeek Harness (upstream fork) — MIT, Copyright (c) 2026 DeepSeek.
- Maya (`python/maya/`) — Apache-2.0.

Vulnerabilities in upstream DeepSeek Harness code should also be reported upstream at <https://github.com/deepseek-ai/deepseek-harness> so the whole community benefits from the fix.
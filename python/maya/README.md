# Maya

Maya is a local, human-supervised Python assistant prototype. It stores its
state in this directory and is designed to run from whichever folder contains
the source; moving or copying the folder does not require editing source paths.

## Setup

Use Python 3.10 or later, then install the small optional runtime dependencies:

```powershell
py -3 -m pip install -r requirements.txt
```

`cryptography` enables encrypted audit records and their tests. `psutil` enables
live resource monitoring. The free-form chat fallback also expects a local
Ollama server with the configured `qwen2.5-coder:3b` model; deterministic
commands remain available when that server is unavailable.

## Run

From this folder:

```powershell
py -3 .\maya_chat.py
# or
py -3 .\maya_app.py
```

The desktop interface starts the colocated Python chat directly; WSL and an
account-specific path are not required. Application control and background
browsing are disabled by default.

## Safety boundary

Maya's learning session is local and explicit. Public research is read-only and
happens only for an explicit topic request. Application control requires an
owner-enabled fixed allowlist, token, confirmation, encryption key, and no
emergency-stop marker.

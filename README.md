# AI-SafeShell 🛡️

**AI-SafeShell** is a protective execution layer designed to stand between AI agents (or humans!) and the operating system. It intercepts commands, validates them against security policies, and prevents destructive or hallucinated operations from harming your system.

---

## The Core Problem
AI coding agents are powerful but can occasionally:
- **Hallucinate** commands that don't exist.
- **Run destructive operations** like `rm -rf /` or `chmod 777`.
- **Lack situational awareness** of the system context (e.g., running clean-up in the wrong directory).

**AI-SafeShell** ensures that execution is never based on blind trust.

---

## Key Features

- **Command Interception**: Every command is intercepted and parsed before reaching the shell.
- **Rule-Based Filtering**:
  - **Hard Block**: Instantly stops dangerous commands (e.g., root deletion).
  - **Confirmation**: Asks the user before running risky operations (e.g., pruning docker).
  - **Auto-Allow**: Passes safe commands through immediately (e.g., `ls`, `git status`).
- **Context Awareness**: Checks system state like current working directory, user identity, and Git repository status to make smarter decisions.
- **Interactive Mode (REPL)**: A persistent shell environment for continuous protected execution.
- **Comprehensive Documentation**: Includes a complete beginner-friendly guidebook and a line-by-line code deep dive.

---

## Tech Stack
- **Language**: Python 3.x
- **Configuration**: YAML (via `PyYAML`)
- **Pattern Matching**: Regex (Python `re` module)
- **OS Interaction**: `subprocess`, `os`, `sys`, `getpass`
### Prerequisites
- Python 3.x
- `pip install PyYAML`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SafeShell.git
   cd SafeShell
   ```
2. Configure your rules in `rules.yaml`.

### Usage

#### One-off Command Check
```bash
python safeshell.py ls -la
```

#### Interactive Mode
Simply run without arguments to start the protected shell:
```bash
python safeshell.py
```

---

## Architecture
- **`safeshell.py`**: The entry point and command wrapper.
- **`engine.py`**: The logic layer that matches commands against rules.
- **`context.py`**: Gathers system metadata for context-aware validation.
- **`rules.yaml`**: The security policy configuration file.
---

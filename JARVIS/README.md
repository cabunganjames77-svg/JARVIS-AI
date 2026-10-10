# JARVIS AI Assistant Starter

A clean Python starter structure for building a personal voice-enabled AI assistant.

## Requirements
- Python 3.10+
- Windows + VS Code (recommended)
- An AI provider API key if you choose to add a cloud model

## Setup (Windows PowerShell)
1. Open this folder in VS Code.
2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and add your settings if needed.
5. Run the starter app:

   ```powershell
   python main.py
   ```

## Project layout
- `src/core/` - assistant orchestration
- `src/voice/` - speech input/output integration points
- `src/ai/` - AI provider integration point
- `src/commands/` - safe, allowlisted computer actions
- `src/memory/` - conversation history helpers
- `src/utils/` - utilities
- `config/` - application configuration
- `data/` - local runtime data
- `logs/` - runtime logs
- `tests/` - tests

## Safety
This starter does not execute arbitrary shell commands. Add computer-control features only with an explicit allowlist and user confirmation for sensitive actions. Do not commit `.env` or API keys.

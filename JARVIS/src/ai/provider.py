import os


def get_ai_response(prompt: str) -> str:
    """Placeholder AI adapter. Configure a provider before enabling live AI."""
    provider = os.getenv("AI_PROVIDER", "").strip()
    if provider:
        return (
            f"AI provider '{provider}' is configured by name, but no provider adapter "
            "has been added yet. Implement it in src/ai/provider.py."
        )
    return (
        "I'm the JARVIS starter. Live AI isn't connected yet. "
        "You can try 'help', 'time', or 'exit'."
    )

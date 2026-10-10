from datetime import datetime


def run_safe_command(text: str) -> str | None:
    """Run only simple, predefined commands. Never execute arbitrary shell input."""
    command = text.strip().lower()
    if command in {"time", "what time is it", "tell me the time"}:
        return f"The current computer time is {datetime.now().strftime('%I:%M %p')}."
    return None

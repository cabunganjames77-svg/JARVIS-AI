from collections import deque
from typing import Deque

_MESSAGES: Deque[dict[str, str]] = deque(maxlen=50)


def remember(role: str, content: str) -> None:
    _MESSAGES.append({"role": role, "content": content})


def recent_messages(limit: int = 10) -> list[dict[str, str]]:
    return list(_MESSAGES)[-limit:]

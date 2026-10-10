from src.commands.actions import run_safe_command


def test_time_command_returns_response():
    result = run_safe_command("time")
    assert result is not None
    assert "computer time" in result.lower()


def test_unknown_command_is_not_executed():
    assert run_safe_command("delete all files") is None

from src.ai.provider import get_ai_response
from src.commands.actions import run_safe_command
from src.memory.store import remember, recent_messages
from src.voice.speech import listen, speak


class JarvisAssistant:
    def run(self) -> None:
        print("JARVIS starter is ready. Type 'help' for commands or 'exit' to quit.")
        while True:
            try:
                user_text = input("\nYou: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nJARVIS: Goodbye.")
                break

            if not user_text:
                continue
            if user_text.lower() in {"exit", "quit", "bye"}:
                print("JARVIS: Goodbye.")
                break
            if user_text.lower() == "help":
                print("JARVIS: Available commands: help, time, exit. AI and voice integrations are placeholders.")
                continue

            local_result = run_safe_command(user_text)
            if local_result is not None:
                reply = local_result
            else:
                reply = get_ai_response(user_text)

            remember("user", user_text)
            remember("assistant", reply)
            print(f"JARVIS: {reply}")

        # Voice hooks are placeholders for future microphone / speech output integrations.

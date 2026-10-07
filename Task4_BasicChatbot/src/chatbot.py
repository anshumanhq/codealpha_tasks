"""
Basic Chatbot - CodeAlpha Python Internship Task 4
A rule-based chatbot that responds to user inputs using keyword matching.
"""

import json
import random
import re
from pathlib import Path
from datetime import datetime


class BasicChatbot:
    """Rule-based chatbot with keyword matching and fallback responses."""

    def __init__(self, responses_file: Path):
        self.responses_file = responses_file
        self.responses = self._load_responses()
        self.user_name = None

    def _load_responses(self) -> dict:
        """Load response rules from JSON file."""
        if not self.responses_file.exists():
            raise FileNotFoundError(
                f"Responses file not found: {self.responses_file}"
            )
        with open(self.responses_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _normalize(self, text: str) -> str:
        """Lowercase + strip punctuation for matching."""
        return re.sub(r"[^\w\s]", "", text.lower().strip())

    def _match_intent(self, user_input: str) -> str:
        """Find best matching intent based on keyword rules."""
        normalized = self._normalize(user_input)

        name_match = re.search(
            r"(?:my name is|i am|i'm|call me)\s+([a-zA-Z]+)",
            normalized,
        )
        if name_match:
            self.user_name = name_match.group(1).capitalize()
            return random.choice(
                self.responses["greetings_name"]
            ).format(name=self.user_name)

        for intent, data in self.responses["intents"].items():
            for keyword in data["keywords"]:
                if keyword in normalized:
                    return random.choice(data["responses"])

        for intent, data in self.responses["intents"].items():
            for keyword in data["keywords"]:
                if keyword in normalized:
                    response = random.choice(data["responses"])
                    if response == "__TIME__":
                        return f"The current time is {datetime.now().strftime('%I:%M %p')} ⏰"
                    if response == "__DATE__":
                        return f"Today is {datetime.now().strftime('%A, %d %B %Y')} 📅"
                    return response

    def get_response(self, user_input: str) -> str:
        """Public method to get chatbot response."""
        return self._match_intent(user_input)

    def greet(self) -> str:
        """Initial greeting message."""
        return random.choice(self.responses["welcome"])


def main():
    base_dir = Path(__file__).resolve().parent.parent
    responses_file = base_dir / "data" / "responses.json"

    print("=" * 55)
    print("         BASIC CHATBOT - CodeAlpha Task 4")
    print("=" * 55)

    try:
        bot = BasicChatbot(responses_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    print(bot.greet())
    print("(Type 'bye' or 'exit' anytime to quit)\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("Bot: Please type something\n")
                continue

            response = bot.get_response(user_input)
            print(f"Bot: {response}\n")

            if bot._normalize(user_input) in {"bye", "exit", "quit", "goodbye"}:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong ({e}). Try again.\n")


if __name__ == "__main__":
    main()
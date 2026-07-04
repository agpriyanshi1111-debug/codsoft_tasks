"""
CODSOFT - Task 1: Rule-Based Chatbot
--------------------------------------
A simple chatbot that responds to user inputs using pattern matching
(regular expressions) rather than machine learning. It demonstrates the
basics of conversation flow and intent recognition.

Run:
    python chatbot.py
"""

import re
import random
from datetime import datetime

# ---------------------------------------------------------------------
# Rule definitions: each rule is (regex pattern, list of possible replies)
# {} placeholders in replies get filled dynamically where relevant.
# ---------------------------------------------------------------------
RULES = [
    (r"\b(hi|hello|hey|good morning|good evening)\b",
     ["Hello there! How can I help you today?",
      "Hi! What can I do for you?",
      "Hey! Nice to hear from you."]),

    (r"\bhow are you\b",
     ["I'm just a program, but I'm running smoothly! How about you?",
      "Doing great, thanks for asking!"]),

    (r"\byour name\b",
     ["I'm CODSOFT-Bot, a simple rule-based chatbot.",
      "You can call me CODSOFT-Bot."]),

    (r"\b(time)\b",
     ["dynamic_time"]),  # handled specially below

    (r"\b(date|day)\b",
     ["dynamic_date"]),

    (r"\bweather\b",
     ["I can't check live weather yet, but I hope it's sunny where you are!"]),

    (r"\b(thank you|thanks)\b",
     ["You're welcome!", "Anytime!", "Glad I could help."]),

    (r"\b(bye|goodbye|exit|quit)\b",
     ["exit"]),  # handled specially below

    (r"\bhelp\b",
     ["I can chat about greetings, tell you the time/date, or just talk. "
      "Type 'bye' to exit."]),

    (r"\bwho (made|created) you\b",
     ["I was built as part of the CodSoft AI Internship, Task 1!"]),
]

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting! Tell me more.",
    "I don't have a rule for that yet, but I'm learning!",
]


def get_response(user_input: str) -> str:
    """Match user input against known rules and return an appropriate reply."""
    text = user_input.lower().strip()

    for pattern, responses in RULES:
        if re.search(pattern, text):
            choice = random.choice(responses)

            if choice == "dynamic_time":
                return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
            if choice == "dynamic_date":
                return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
            if choice == "exit":
                return "__EXIT__"

            return choice

    return random.choice(DEFAULT_RESPONSES)


def main():
    print("CODSOFT-Bot: Hello! I'm a rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue

        reply = get_response(user_input)
        if reply == "__EXIT__":
            print("CODSOFT-Bot: Goodbye! Have a great day.")
            break

        print(f"CODSOFT-Bot: {reply}")


if __name__ == "__main__":
    main()

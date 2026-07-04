# Task 1 — Rule-Based Chatbot

## Objective
Build a simple chatbot that responds to user inputs based on predefined
rules, using pattern matching to identify intents and generate replies.

## Approach
- Uses Python's `re` module for pattern matching (regular expressions).
- A list of `(pattern, responses)` rules covers common intents: greetings,
  small talk, time/date queries, thanks, and exit commands.
- Falls back to a generic response when no rule matches.
- Some responses are dynamic (e.g., current time/date).

## How to run
```bash
python chatbot.py
```

Then chat with the bot in the terminal. Type `bye`, `exit`, or `quit` to end
the conversation.

## Example
```
CODSOFT-Bot: Hello! I'm a rule-based chatbot. Type 'bye' to exit.
You: hi
CODSOFT-Bot: Hi! What can I do for you?
You: what time is it
CODSOFT-Bot: The current time is 14:32:10.
You: bye
CODSOFT-Bot: Goodbye! Have a great day.
```

## Concepts demonstrated
- Basic NLP via regex-based intent matching
- Conversation loop / state handling
- Extensible rule design (easy to add new intents)

## Possible extensions
- Add NLTK/spaCy for tokenization and stemming
- Add fuzzy matching for typos
- Wrap in a Flask web UI

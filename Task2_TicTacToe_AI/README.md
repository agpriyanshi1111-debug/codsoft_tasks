# Task 2 — Tic-Tac-Toe AI

## Objective
Implement an AI agent that plays Tic-Tac-Toe against a human player, using
the Minimax algorithm (with Alpha-Beta Pruning) so the AI is unbeatable.

## Approach
- Board represented as a list of 9 cells (`" "`, `"X"`, `"O"`).
- `minimax()` recursively explores all possible future game states, scoring:
  - `+10 - depth` if the AI wins (prefers faster wins)
  - `depth - 10` if the human wins (prefers slower losses)
  - `0` for a draw
- Alpha-beta pruning cuts off branches that can't affect the final decision,
  speeding up the search.
- `best_move()` picks the move with the highest minimax score for the AI.

## How to run
```bash
python tic_tac_toe.py
```
You'll be prompted to enter a position (0–8) on each of your turns; the AI
responds automatically and cannot be beaten (best case for you is a draw).

## Concepts demonstrated
- Game trees and adversarial search
- Minimax algorithm
- Alpha-beta pruning optimization

## Possible extensions
- Add a GUI (Tkinter / Pygame)
- Support different board sizes (e.g., 4x4, N-in-a-row)
- Add difficulty levels (limit search depth for an easier AI)

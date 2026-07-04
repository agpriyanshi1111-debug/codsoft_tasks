"""
CODSOFT - Task 2: Tic-Tac-Toe AI
-----------------------------------
An unbeatable Tic-Tac-Toe AI implemented using the Minimax algorithm
with Alpha-Beta Pruning.

Run:
    python tic_tac_toe.py
"""

import math

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(" | ".join(row))
        if i < 6:
            print("--+---+--")
    print()


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def is_full(board):
    return EMPTY not in board


def minimax(board, depth, is_maximizing, alpha, beta):
    if winner(board, AI):
        return 10 - depth
    if winner(board, HUMAN):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def best_move(board):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice


def main():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe: You are 'X', the AI is 'O'.")
    print("Board positions are numbered 0-8 (left to right, top to bottom).")
    print_board([str(i) for i in range(9)])

    current_player = HUMAN

    while True:
        if current_player == HUMAN:
            try:
                move = int(input("Your move (0-8): "))
            except ValueError:
                print("Please enter a number between 0 and 8.")
                continue
            if move not in available_moves(board):
                print("Invalid move. Try again.")
                continue
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = best_move(board)
            board[move] = AI
            print(f"AI plays position {move}.")

        print_board(board)

        if winner(board, current_player):
            print(f"{current_player} wins!" if current_player == HUMAN
                  else "AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

        current_player = AI if current_player == HUMAN else HUMAN


if __name__ == "__main__":
    main()

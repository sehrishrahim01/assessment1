import random
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def find_winner(board):
    for line in WIN_LINES:
        a, b, c = line

        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a], line

    return None, None
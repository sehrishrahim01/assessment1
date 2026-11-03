import random
from flask import Flask, jsonify, request
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]
def winner(board):
    for x, y, z in WIN_LINES:
        if board[x] != " " and board[x] == board[y] == board[z]:
            return board[x]
    return None
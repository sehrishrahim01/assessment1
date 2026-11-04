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
def minimax(board, turn, me, opp, alpha, beta, depth):
    w = winner(board)
    if w == me:
        return 10 - depth
    if w == opp:
        return depth - 10
    if " " not in board:
        return 0
    moves = [
        i for i, value in enumerate(board)
        if value == " "
    ]
    if turn == me:
        best = -100
        for move in moves:
            board[move] = me
            score = minimax(
                board,opp,me,opp,alpha,beta,depth + 1
            )
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    best = 100
    for move in moves:
        board[move] = opp
        score = minimax(
            board,me,me,opp,alpha,beta,depth + 1
        )
        board[move] = " "
        best = min(best, score)
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


  


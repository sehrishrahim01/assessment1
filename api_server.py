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
def best_move(board, me):
    opp = "X" if me == "O" else "O"
    scored_moves = []
    available_moves = [
        i for i, value in enumerate(board)
        if value == " "
    ]
    for move in available_moves:
        board[move] = me
        score = minimax(
            board,opp,me,opp,-100,100,1
        )
        board[move] = " "
        scored_moves.append((score, move))
    if not scored_moves:
        return None
    best_score = max(score for score, move in scored_moves)
    best_moves = [
        move for score, move in scored_moves
        if score == best_score
    ]
    return random.choice(best_moves)




  


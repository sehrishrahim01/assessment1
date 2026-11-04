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
    
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def get_move(board, player_name):
    while True:
        try:
            move = int(input(f"{player_name}, enter position (1-9): "))

            if move < 1 or move > 9:
                print("Invalid position. Choose between 1 and 9.")
                continue

            index = move - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            return index

        except ValueError:
            print("Please enter a valid number.")


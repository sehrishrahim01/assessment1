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
def play_game(mode, player_name):
    board = [" "] * 9
    players = {
        "X": player_name,
        "O": "Computer" if mode == "computer" else "Friend"
    }
    turn = "X"
    game_over = False
    while not game_over:
        display_board(board)
        print(f"{players[turn]}'s turn ({turn})")
        if mode == "computer" and turn == "O":
            move = computer_move(board)
            print(f"Computer chooses position {move + 1}")
        else:
            move = get_move(board, players[turn])
        board[move] = turn
        winner, line = find_winner(board)
        if winner:
            display_board(board)
            print(f"{players[winner]} ({winner}) wins!")
            game_over = True
        elif " " not in board:
            display_board(board)
            print("It's a draw!")
            game_over = True
        else:
            turn = "O" if turn == "X" else "X"



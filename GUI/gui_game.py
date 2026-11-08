import random
import tkinter as tk
from tkinter import messagebox
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
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.resizable(False, False)
        self.menu_frame = tk.Frame(self, padx=30, pady=20)
        self.game_frame = tk.Frame(self, padx=20, pady=20)

        self.build_menu()
        self.build_game()
        self.show_menu()

    def build_menu(self):
        f = self.menu_frame
        tk.Label(
            f,text="TIC TAC TOE",
            font=("Arial", 24, "bold")
        ).pack(pady=(0, 15))
        tk.Label(f, text="Your name (X):").pack()
        self.name_var = tk.StringVar(value="Player")
        tk.Entry(
            f,textvariable=self.name_var,
            justify="center"
        ).pack(pady=(0, 10))
        tk.Button(
            f,text="Play with Friend",
            width=22,
            command=lambda: self.start("friend")
        ).pack(pady=3)
        tk.Button(
            f,text="Play with Computer",
            width=22,
            command=lambda: self.start("computer")
        ).pack(pady=3)
        tk.Button(
            f,text="Quit",
            width=22,
            command=self.destroy
        ).pack(pady=3)




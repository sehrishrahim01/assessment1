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
    def build_game(self):
        f = self.game_frame
        self.status = tk.Label(
            f,
            text="",
            font=("Arial", 14)
        )
        self.status.pack(pady=(0, 10))
        grid = tk.Frame(f)
        grid.pack()
        self.buttons = []
        for i in range(9):
            b = tk.Button(
                grid,
                text="",
                width=4,
                height=2,
                font=("Arial", 28, "bold"),
                command=lambda i=i: self.on_click(i)
            )
            b.grid(
                row=i // 3,
                column=i % 3,
                padx=2,
                pady=2
            )
            self.buttons.append(b)
        bar = tk.Frame(f)
        bar.pack(pady=(10, 0))
        tk.Button(
            bar,
            text="Restart",
            command=lambda: self.start(self.mode)
        ).pack(side="left", padx=5)
        tk.Button(
            bar,
            text="Menu",
            command=self.show_menu
        ).pack(side="left", padx=5)
    def show_menu(self):
        self.game_frame.pack_forget()
        self.menu_frame.pack()
    def start(self, mode):
        self.mode = mode
        self.name = self.name_var.get().strip() or "Player"
        self.p_names = {
            "X": self.name,
            "O": "Computer" if mode == "computer" else "Friend"
        }
        self.board = [" "] * 9
        self.turn = "X"
        self.over = False

        for b in self.buttons:
            b.config(
                text="",
                state="normal",
                bg="#d9d9d9"
            )
        self.menu_frame.pack_forget()
        self.game_frame.pack()
        self.update_status()
    def update_status(self):
        self.status.config(
            text=f"{self.p_names[self.turn]}'s turn ({self.turn})"
        )
    def on_click(self, i):
        if self.over or self.board[i] != " ":
            return
        if self.mode == "computer" and self.turn == "O":
            return
        self.place(i)
        if not self.over and self.mode == "computer":
            self.after(400, self.computer_turn)

    def place(self, i):
        self.board[i] = self.turn

        self.buttons[i].config(
            text=self.turn,
            fg="#d33" if self.turn == "X" else "#33d"
        )
        w, line = find_winner(self.board)

        if w:
            self.finish(w, line)

        elif " " not in self.board:
            self.finish(None, None)

        else:
            self.turn = "O" if self.turn == "X" else "X"
            self.update_status()

    def computer_turn(self):
        if self.over:
            return
        available_moves = [
            i for i, value in enumerate(self.board)
            if value == " "
        ]
        if not available_moves:
            return
        move = random.choice(available_moves)
        self.place(move)

    def finish(self, w, line):
        self.over = True
        for b in self.buttons:
            b.config(state="disabled")
        if line:
            for i in line:
                self.buttons[i].config(bg="#8f8")
            msg = f"{self.p_names[w]} ({w}) wins!"
        else:
            msg = "It's a draw!"
        self.status.config(text=msg)
        messagebox.showinfo("Game over", msg)

if __name__ == "__main__":
    App().mainloop()


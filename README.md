# Tic Tac Toe Game

## Project Overview

Tic Tac Toe is a Python based game developed as a programming project. It allows two players to play against each other or a single player to play against the computer.

The project provides two interfaces: a Graphical User Interface (GUI) developed using Tkinter and a Command Line Interface (CLI) that runs in the terminal.

## Features

1. Play with a Friend
2. Play with Computer
3. Graphical User Interface using Tkinter
4. Command Line Interface using Python
5. Player Name Input
6. Automatic Winner Detection
7. Draw Detection
8. Restart Game Option
9. Return to Main Menu

## Technologies Used

**Programming Language:** Python 3

**GUI Library:** Tkinter

**Additional Module:** Random

## Project Structure

```text
Tic-Tac-Toe/
│
├── GUI/
│   └── gui_game.py
│
├── CLI/
│   └── cli_game.py
│
├── README.md
└── .gitignore
```

## Installation

Make sure Python 3 is installed on your system.

Tkinter is generally included with standard Python installations. On Ubuntu or Debian, install it using:

```bash
sudo apt install python3-tk
```

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd Tic-Tac-Toe
```

## How to Run

### Graphical Version

Run the following command:

```bash
python GUI/gui_game.py
```

### Command Line Version

Run the following command:

```bash
python CLI/cli_game.py
```

## Game Instructions

1. Start the game using either the GUI or CLI version.
2. Enter your player name.
3. Select Play with Friend or Play with Computer.
4. Players take turns selecting positions on the 3 × 3 board.
5. The first player to complete a horizontal, vertical, or diagonal line wins.
6. If all positions are filled without a winner, the game ends in a draw.

## Learning Outcomes

This project demonstrates the practical implementation of fundamental Python programming concepts, including:

1. Functions and Modular Programming
2. Classes and Object Oriented Programming
3. Conditional Statements and Loops
4. Lists and List Indexing
5. Random Module
6. Exception Handling
7. Event Handling
8. GUI Development using Tkinter

## Author

**Sehrish Rahim**



## License

This project is developed for educational and academic purposes.
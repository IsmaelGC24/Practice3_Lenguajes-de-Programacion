Solution for Programming Languages ​​Practice 3. Created by: Ismael García Ceballos and Kevin Eduardo Hernández Durango.

Video link: 

# Chess Game Tree - Readme

## Project Description

This project implements a console-based chess game in Python. It allows users to input moves in SAN (Standard Algebraic Notation) and visualizes the sequence of moves as a binary tree.

Each move is stored in a tree structure:

* The **left branch** represents moves made by White.
* The **right branch** represents moves made by Black.

Users can view the current state of the board, print the full list of moves in PGN format using the `resultado` command, or display the move tree with the `árbol` command. The game continues until the user types `salir`.

The `python-chess` library is used to manage board state, validate legal moves, and display the board using Unicode characters.

## Features

* Interactive move input using SAN notation
* Binary tree representation of the game
* PGN-style move summary
* Custom board rendering using Unicode

## Language and Environment

* Language: Python 3
* Interpreter: CPython 3.x
* IDE: Replit ([https://replit.com](https://replit.com))

## Dependencies

* `python-chess` (install with: `pip install python-chess`)

## How to Run

1. Make sure to install the required package:

   ```bash
   pip install python-chess
   ```
2. Run the script in Replit or any Python 3-compatible environment.

---

This project was developed as part of a programming practice assignment.

# Tic-Tac-Toe Using Python

## Overview

This is a Python implementation of the classic Tic-Tac-Toe game for two players.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/tictactoe.git
    ```

2. Navigate to the project directory:

    ```sh
    cd tictactoe
    ```

3. Ensure `helpers.py` is in the same directory as `main.py`.

## Usage

Run the main script to start the game:

```sh
python main.py
```

## Files
- main.py: Main script to run the game.
- helpers.py: Contains helper functions for game logic.

## Functions in helpers.py
- draw_board(spots): Draws the current state of the board.
- check_turn(turn): Returns 'X' or 'O' based on the turn.
- check_for_win(spots): Checks if there's a winner.

## Game Instructions
- Players take turns to pick a spot by entering a number (1-9).
- The game announces the winner or declares a draw when the board is full.

## Example
```sh
$ python main.py
```

```yaml
Welcome to Tic-Tac-Toe!
Player 1: X
Player 2: O

|1|2|3|
|4|5|6|
|7|8|9|

Player 1, choose your position (1-9): 5
```

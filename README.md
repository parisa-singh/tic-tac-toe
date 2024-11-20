# Tic-Tac-Toe Game
## Overview

This is a Python implementation of the classic **Tic-Tac-Toe** game. It supports dynamic board sizes (`n x n`) and allows two players to compete by alternately placing their tokens (`X` and `O`). The first player to align their tokens in a row, column, or diagonal wins the game.

## Features

- **Dynamic Board Size**: Specify any board size (e.g., 3x3, 4x4, etc.) at the start of the game.
- **Interactive Gameplay**: Players are prompted to select their moves until there is a winner or the game ends in a tie.
- **Winning Conditions**:
  - Align all tokens in a row.
  - Align all tokens in a column.
  - Align all tokens in the main diagonal.
  - Align all tokens in the anti-diagonal.
- **Input Validation**: Ensures that players provide valid and available locations.

## Requirements

- Python 3.x

## How to Play

1. **Start the Game**  
   Run the script in a terminal or IDE. For a standard 3x3 game, the function `play_game(3)` is already called in the script.

2. **Board Initialization**  
   The game will print an empty board with spaces for tokens.

3. **Player Turns**  
   - Players alternate turns, starting with `X`.
   - Each turn, the player is prompted to enter a row and column index to place their token.
   - The game will validate the input and update the board if the move is valid.

4. **Winning and Tie Conditions**  
   - A player wins if they align their tokens in a row, column, or diagonal.
   - If all spaces are filled and no player wins, the game ends in a tie.

## Example Gameplay

### 3x3 Game Initialization
```
*** Welcome to 3 by 3 Tic-Tac-Toe ***
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

### Player Move
```
* X's turn *
Please enter a row index between 0 and 2: 1
Please enter a column index between 0 and 2: 1

+---+---+---+
|   |   |   |
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

---

## Functions Explained

1. **`make_empty_board(n)`**: Creates an `n x n` board filled with empty spaces.
2. **`print_board(n, board)`**: Displays the current state of the board.
3. **`get_location(n, board)`**: Prompts the current player for a valid move.
4. **`row_win(n, board, player)`**: Checks if the player has aligned tokens in any row.
5. **`col_win(n, board, player)`**: Checks if the player has aligned tokens in any column.
6. **`diag_win(n, board, player)`**: Checks if the player has aligned tokens in the main diagonal.
7. **`anti_diag_win(n, board, player)`**: Checks if the player has aligned tokens in the anti-diagonal.
8. **`has_won(n, board, player)`**: Combines all win conditions to determine if a player has won.
9. **`play_game(n)`**: Manages the overall gameplay loop.

## Customization

To play on a different board size, modify the argument in the `play_game()` function.  
Example: For a 4x4 board, use `play_game(4)`.

## Contributions

Feel free to fork this repository, suggest improvements, or report any issues via GitHub or email.

## License

This project is open-source and available under the MIT License.

def print_board(n, board):
    # premake +---+ style boundary using string mutiplication and concatination
    boundary_line = ("+---" * n) + "+"
    # range over every row in board (an n by n board)
    for i in range(n):
        # print a leading boundary line
        print(boundary_line)
        # start string for row i with leading bar
        row_i = "|"
        # range over every column in board (an n by n board)
        for j in range(n):
            # update row_i string with space, characher from board, space, and trailing bar
            # this completes "cell j" for row i
            row_i += " " + board[i][j] + " " + "|"
        # print the completed row i
        print(row_i)
    # print final boundary line
    print(boundary_line)

def make_empty_board(n):
    """Creates an n x n board with empty spaces."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def get_location(n, board):
    """Prompts user for a valid row and column to place their token."""
    while True:
        row = input(f"Please enter a row index between 0 and {n-1}: ")
        col = input(f"Please enter a column index between 0 and {n-1}: ")

        if not (row.isdigit() and col.isdigit()):
            print(f"({row}, {col}) is not a legal input!")
            continue

        row, col = int(row), int(col)

        if not (0 <= row < n and 0 <= col < n):
            print(f"({row}, {col}) is not a legal space!")
        elif board[row][col] != ' ':
            print(f"({row}, {col}) is not an available space!")
        else:
            return row, col

def row_win(n, board, player):
    """Checks if there is a winning row for the player."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False

def col_win(n, board, player):
    """Checks if there is a winning column for the player."""
    for col in range(n):
        if all(board[row][col] == player for row in range(n)):
            return True
    return False

def diag_win(n, board, player):
    """Checks if there is a winning diagonal for the player."""
    return all(board[i][i] == player for i in range(n))

def anti_diag_win(n, board, player):
    """Checks if there is a winning anti-diagonal for the player."""
    return all(board[i][n - 1 - i] == player for i in range(n))

def has_won(n, board, player):
    """Determines if the player has won by any method."""
    return row_win(n, board, player) or col_win(n, board, player) or diag_win(n, board, player) or anti_diag_win(n, board, player)

def play_game(n):
    """Controls the flow of the Tic-Tac-Toe game."""
    print(f"*** Welcome to {n} by {n} Tic-Tac-Toe ***")
    board = make_empty_board(n)
    print_board(n, board)

    players = ['X', 'O']
    turn_count = 0
    max_turns = n * n

    while turn_count < max_turns:
        current_player = players[turn_count % 2]
        print(f"\n* {current_player}'s turn *")
        row, col = get_location(n, board)
        board[row][col] = current_player
        print_board(n, board)

        if has_won(n, board, current_player):
            print(f"{current_player} wins!")
            return
        turn_count += 1

    print("Tie!")

# Example of running the game with a 3x3 board
play_game(3)

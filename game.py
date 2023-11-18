def create_board():
    """Creates an empty 3x3 tic-tac-toe board."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    """Prints the tic-tac-toe board."""
    for row in board:
        print("| " + " | ".join(row) + " |")

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check for horizontal wins
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check for vertical wins
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check for diagonal wins
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def make_move(board, player, row, col):
    """Makes a move on the board for the given player."""
    if board[row][col] != " ":
        return False

    board[row][col] = player
    return True

def switch_player(current_player):
    """Switches the current player."""
    if current_player == "X":
        return "O"
    else:
        return "X"

def play_game():
    """Plays a tic-tac-toe game."""
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        print(f"Player {current_player}'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if not make_move(board, current_player, row, col):
            print("Invalid move. Try again.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        current_player = switch_player(current_player)

        # Check if all cells are filled
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

play_game()

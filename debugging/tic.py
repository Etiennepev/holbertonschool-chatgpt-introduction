#!/usr/bin/python3

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there's a winner."""

    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True


    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True


    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def valid_input():
    """Ensures that the input is a valid integer within the range 0-2."""
    while True:
        try:
            value = int(input("Enter row/column (0, 1, or 2): "))
            if value < 0 or value > 2:
                print("Invalid input! Please enter a number between 0 and 2.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

def tic_tac_toe():
    """Runs the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        print(f"Player {player}'s turn.")
        

        row = valid_input()
        col = valid_input()


        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
    
    print_board(board)

    print(f"Player {player} wins!")

if __name__ == "__main__":
    tic_tac_toe()

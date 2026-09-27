N = 8


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col):
    # Check the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False

        i -= 1
        j += 1

    return True


def solve(board, row):
    # All queens have been placed
    if row == N:

        
        return True

    # Try every column in this row
    for col in range(N):

        if is_safe(board, row, col):

            # Place queen
            board[row][col] = "Q"

            # Try the next row
            if solve(board, row + 1):
                return True

            # Backtrack
            board[row][col] = "."

    return False


# Create an empty 8x8 board
board = [["." for _ in range(N)] for _ in range(N)]


# Solve the problem
if solve(board, 0):
    print("N-Queens Solution:")
    print_board(board)
else:
    print("No solution found.")
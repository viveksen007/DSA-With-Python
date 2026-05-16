def is_safe(row, col, board, n):
    # Check upper column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_N_Queens(row, board, ans, n):
    if row == n:
       copy = ["".join(row) for row in board]
       ans.append(copy)
       return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 'Q'
            solve_N_Queens(row + 1, board, ans, n)
            board[row][col] = '.'  # Backtrack

# Example usage
n = 4
board = ['.'*n for _ in range(n)]
ans = []
solve_N_Queens(0, board, ans, n)

for solution in ans:
    for row in solution:
        print(row)
    print()

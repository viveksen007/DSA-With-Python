import tkinter as tk

def DisplaySudoku(board):
    root = tk.Tk()
    root.title("Sudoku Solver")

    for i in range(9):
        for j in range(9):
            cell = tk.Entry(root, width=2, font=('Arial', 18), justify='center')
            cell.grid(row=i, column=j, padx=2, pady=2)
            val = board[i][j]
            if val != 0:
                cell.insert(0, str(val))
                cell.config(state='readonly')

    root.mainloop()

def Sudoku_Solver(board):
    Solve(board)

def IsValid(board, row, col, n):
    for i in range(9):
        if board[i][col] == n:
            return False
        if board[row][i] == n:
            return False
        if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == n:
            return False
    return True

def Solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if IsValid(board, i, j, k):
                        board[i][j] = k
                        if Solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True


def PrintBoard(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


if __name__ == "__main__":
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    
    Solve(board)
    print(board)
   
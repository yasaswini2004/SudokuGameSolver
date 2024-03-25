#To make the 9*9 board into partitions of 3*3
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid(board, num, row, col):
    # Check if the number already exists in the row
    if num in board[row]:
        return False
    
    # Check if the number already exists in the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number already exists in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    if row is None and col is None:
        return True  # Puzzle solved
    
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack if the solution is not valid
    return False

def input_board():
    board = []
    print("Enter the Sudoku puzzle row by row, with each row separated by spaces.")
    print("Use '0' to represent empty cells.")
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

# Taking input Sudoku board from the user
board = input_board()

print("\nSudoku puzzle:")
print_board(board)
print("\nSolving...\n")
if solve_sudoku(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists.")

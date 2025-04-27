'''
1. Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
according to the following constraints.
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other.


import random

def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def is_safe(board, row, col, n):
    Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

     Check the upper-right diagonal
     i, j = row, col
     while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        print()
        return True

  found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            found_solution = solve_n_queens(board, row + 1, n) or found_solution
            board[row][col] = 0  #

    return found_solution

def n_queens():
    n = random.randint(4, 10)  # Randomly selects number of queens (between 4 and 10)
    print(f"Number of queens: {n}")
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

# Solve the N-Queens Problem with a random number of queens
n_queens()
'''
i=8,j=8
for k in range(i):
    for k in range(j):
matrix = [[0 for _ in range(8)] for _ in range(8)]

for row in matrix:
    print(row)
def check_column:

def check_row:

def top_left_diagonal:

def top_right_diagonal:
import random
def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def is_safe(board, row, col, n):
    Check the column
    for i in range(row):
     if board[i][col]
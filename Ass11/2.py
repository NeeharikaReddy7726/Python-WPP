import numpy as np
import matplotlib.pyplot as plt

N = 8   
def solveNQueens(board, col):
    if col == N:
        printing(board)   
        return True
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place a queen at (i, col)
            if solveNQueens(board, col + 1):  # Recursively try to place queens in the next column
                return True
            board[i][col] = 0  # Backtrack if no solution is found
    
    return False

def isSafe(board, row, col):
    # Check the row on the left side
    for x in range(col):
        if board[row][x] == 1:
            return False
    
    # Check the upper diagonal on the left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    
    # Check the lower diagonal on the left side
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    
    return True

def printing(board):
    for i in range(8):
        for j in range(8):
            if(board[i,j]==1):
                print('Q ' ,end='')
            else:
                print('. ',end='')
        print()
 
 
board = np.zeros((N, N), dtype=int)
if not solveNQueens(board, 0):
    print("No solution found")
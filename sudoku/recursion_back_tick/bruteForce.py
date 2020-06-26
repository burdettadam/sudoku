''' 
takes point in grid(x,y) and value (n) to be validated.
returns True or False
'''
import numpy as np

grid = [ [1,2,3,  4,5,6,  7,8,9],
         [4,5,0,  7,8,9,  1,2,3],
         [7,8,9,  1,2,3,  4,5,6],
         [2,3,4,  5,6,7,  8,9,1],
         [5,6,7,  8,9,1,  2,3,4],
         [8,9,1,  2,3,4,  5,6,7],
         [3,4,5,  6,7,8,  9,1,2],
         [6,7,8,  9,1,2,  3,4,5],
         [9,1,2,  3,4,5,  6,7,8]]

def validate(col,row,n):
    #check col
    for i in range(0,9): #0,...,8
        if grid[col][i] == n:
            return False
    #check row
    for i in range(0,9):
        if grid[i][row] == n:
            return False
    #check square
    xo = int(row/3)*3 # is 0,3,6
    yo = int(col/3)*3
    for i in range(0,3): # 0,1
        for j in range(0,3):
            if grid[yo+i][xo+j] == n:
                return False
    return True

grid = [ [1,2,0,  4,0,6,  7,8,9],
         [4,0,6,  7,8,9,  1,2,3],
         [7,8,9,  1,2,3,  4,5,6],
         [2,3,4,  5,6,7,  8,9,1],
         [5,6,7,  8,9,1,  2,3,4],
         [8,9,1,  2,3,4,  5,6,7],
         [3,4,5,  6,7,8,  9,1,2],
         [6,7,8,  9,1,2,  3,4,5],
         [9,1,2,  3,4,5,  6,7,8]]

def solve():
    """ Add a doc comment? """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: # not a clue
                for n in range(1,10): # try all possible solutions
                    if validate(row,col,n): # works ?
                        grid[row][col] = n # add solution
                        solve()
                        grid[row][col] = 0 # failed attempts return here and back tick,
                return # basecase,return out of recurssion
    print(np.matrix(grid)) # print winners
print(solve()) # solve() returns None so this just prints None

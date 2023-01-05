
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    dominate = 0
    is_big = False
    if(len(grid) == 0 ):
        return 0
    try:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(len(grid[i]) != 0):
                    if(i!=0 and j!=0 and i!=len(grid)-1 and j!=len(grid[i])-1):
                        if(grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i][j-1]):
                            dominate+=1
                    elif(i==0 and j==0):
                        if(grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j+1]):
                            dominate+=1
                    elif(i==0 and j==len(grid[i])-1):
                        if(grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i+1][j]):
                            dominate+=1
                    elif(i==len(grid)-1 and j==len(grid[i])-1):
                        if(grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i-1][j]):
                            dominate+=1
                    elif(i==len(grid)-1 and j==0):
                        if(grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i][j+1]):
                            dominate+=1
                    elif(i==0 and j>0 and j<len(grid[i])-1):
                        if(grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i+1][j]):
                            dominate+=1
                    elif(i==len(grid)-1 and j>0 and j<len(grid[i])-1):
                        if(grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i-1][j]):
                            dominate+=1
                    elif(j==len(grid[i])-1 and i>0 and i<len(grid)-1):
                        if(grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1]):
                            dominate+=1
                    elif(j==0 and i>0 and i<len(grid)-1):
                        if(grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j+1]):
                            dominate+=1

    except:
        for i in range(len(grid)):
            if(i==0):
                if(grid[i]>grid[i+1]):
                    dominate+=1
            elif(i==len(grid)-1):
                if(grid[i]>grid[i-1]):
                    dominate+=1
            else:
                if(grid[i]>grid[i-1] and grid[i]>grid[i+1]):
                    dominate+=1


    return dominate

grid =[[9 ,1, 1],
       [1 ,1, 9],
       [9, 1, 1],
       [1, 1, 9]]
print(numCells([1,2,2,9]))

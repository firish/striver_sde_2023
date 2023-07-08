from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    if n == 1: return [[1]]
    elif n == 2: return [[1], [1, 1]]
    else:
        pascal = [[1], [1, 1]]
        for _ in range(3, n+1, 1):
            row = [1]
            for i in range(0, len(pascal[-1])-1, 1):
                row.append(pascal[-1][i] + pascal[-1][i+1])
            row.append(1)
            pascal.append(row)
        return pascal


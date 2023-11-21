from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    rows = {}
    cols = {}

    def set_row_zero(matrix, row, m):
        for c in range(0, m, 1): matrix[row][c] = 0
    
    def set_col_zero(matrix, col, n):
        for r in range(0, n, 1): matrix[r][col] = 0
    
    n, m = len(matrix), len(matrix[0])
    for row in range(0, n, 1):
        for col in range(0, m, 1):
            if (matrix[row][col] == 0):
                rows[row] = 1
                cols[col] = 1
    
    for row in rows.keys(): set_row_zero(matrix, row, m)
    for col in cols.keys(): set_col_zero(matrix, col, n)
    return matrix
                

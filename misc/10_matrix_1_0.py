# Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from collections import defaultdict

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows_0, rows_1 = defaultdict(int), defaultdict(int)
        cols_0, cols_1 = defaultdict(int), defaultdict(int)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows_1[r] += 1
                    cols_1[c] += 1
                else:
                    rows_0[r] += 1
                    cols_0[c] += 1
        
        diff = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                diff[r][c] = rows_1[r] + cols_1[c] - rows_0[r] - cols_0[c]
        return diff

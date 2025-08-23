# LC 695 (Medium)
# Max Area of a Island
# URL: https://leetcode.com/problems/max-area-of-island/

# My Soln
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def is_valid(row, col):
            return True if 0 <= row < m and 0 <= col < n else False
        
        def is_land(row, col):
            return grid[row][col] == 1

        def dfs(row, col):
            seen.add((row, col))
            for d in dirs:
                r, c = d
                row2, col2 = row + r, col + c
                if is_valid(row2, col2) and is_land(row2, col2) and (row2, col2) not in seen:
                    current_area[0] += 1
                    seen.add((row2, col2))
                    dfs(row2, col2)
        
        # traverse the grid
        current_area = [0]
        largest_area = 0
        seen = set()
        for row in range(m):
            for col in range(n):
                if is_land(row, col) and (row, col) not in seen:
                    dfs(row, col)
                    largest_area = max(largest_area, current_area[0]+1)
                    current_area[0] = 0
        return largest_area


# Link: https://leetcode.com/problems/unique-paths-ii/submissions/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return 0
        
        def is_valid(r, c, m, n, grid):
            if 0 <= r < m and 0 <= c < n and grid[r][c] != 1: return True
            return False
        
        def travel(r, c, m, n, dp):
            if (r, c) == (m-1, n-1):
                if grid[r][c] == 1:
                    return 0
                return 1
            
            # memo check
            if dp[r][c] != -1:
                return dp[r][c]
            
            right, down = 0, 0
            # go right
            if is_valid(r+0, c+1, m, n, grid):
                right = travel(r+0, c+1, m, n, dp)
            # go down
            if is_valid(r+1, c+0, m, n, grid):
                down = travel(r+1, c+0, m, n, dp)
            
            # memoize
            dp[r][c] = right + down
            return dp[r][c]
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return travel(0, 0, m, n, dp)

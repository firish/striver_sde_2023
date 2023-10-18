# Link: https://leetcode.com/problems/minimum-path-sum/submissions/



class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def is_valid(r, c, m, n):
            if 0 <= r < m and 0 <= c < n: return True
            return False
        
        def path_sum(r, c, m, n, dp):
            if r == 0 and c == 0:
                return grid[r][c]
            
            # memo check
            if dp[r][c] != 10**12:
                return dp[r][c]
            
            up, left = 10**12, 10**12
            if is_valid(r-1, c+0, m, n):
                up = grid[r][c] + path_sum(r-1, c+0, m, n, dp)
            if is_valid(r+0, c-1, m, n):
                left = grid[r][c] + path_sum(r+0, c-1, m, n, dp)
            
            # memoize
            dp[r][c] = min(up, left)
            return dp[r][c]
        
        dp = [[10**12 for _ in range(n)] for _ in range(m)]
        return path_sum(m-1, n-1, m, n, dp)



# tabulate
m, n = len(grid), len(grid[0])
dp = [[10**12 for _ in range(n)] for _ in range(m)]
for r in range(m):
    for c in range(n):
        if r == 0 and c == 0:
            dp[r][c] = grid[r][c]
        else:
            up = grid[r][c]+ dp[r-1][c+0]
            left = grid[r][c]+ dp[r+0][c-1]
            dp[r][c] = min(up, left)
return dp[m-1][n-1]

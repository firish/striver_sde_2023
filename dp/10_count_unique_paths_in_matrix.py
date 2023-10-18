# Link: https://leetcode.com/problems/unique-paths/discuss/4180963/Python-memoization-template-clean-and-simple.
# 2d DP question

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def is_valid(r, c, m, n):
            if 0 <= r < m and 0 <= c < n: return True
            return False
        
        def travel(r, c, m, n, dp):
            if (r, c) == (m-1, n-1):
                return 1
            
            # memo check
            if dp[r][c] != -1:
                return dp[r][c]
            
	    right, down = 0, 0
            # go right
            if is_valid(r+0, c+1, m, n):
                right = travel(r+0, c+1, m, n, dp)
            # go down
            if is_valid(r+1, c+0, m, n):
                down = travel(r+1, c+0, m, n, dp)
            
            # memoize
            dp[r][c] = right + down
            return dp[r][c]
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return travel(0, 0, m, n, dp)


# Tabulating the solution

# steps
# get the base condition
# a for loop for each state (1 for r, 1 for c)
# this is bottom up, mostly copy recurrence relation, sometimes modify it (like this case)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                # base case
                if r == 0 and c == 0: dp[r][c] = 1
                else:
                    up = dp[r-1][c+0]
                    left = dp[r+0][c-1]
                    # tabulate
                    dp[r][c] = up + left
        return dp[m-1][n-1]

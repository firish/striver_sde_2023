# Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(curr, n, dp):
            if curr < 0:
                return 0
            elif curr == 0:
                return 1
            
            if dp[curr] != -1:
                return dp[curr]
            else:
                dp[curr] = climb(curr-1, n, dp) + climb(curr-2, n, dp)
                return dp[curr]
        
        
        dp = [-1]*(n+1)
        return climb(n, n, dp)

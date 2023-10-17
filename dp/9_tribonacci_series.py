# Link: https://leetcode.com/problems/n-th-tribonacci-number/submissions/


class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0, 1, 1] + [-1]*(n-2)
        def get_tribo(ind, dp):
            if ind < 3:
                return dp[ind]
            
            if dp[ind] != -1:
                return dp[ind]
            
            dp[ind] = get_tribo(ind-1, dp) + get_tribo(ind-2, dp) + get_tribo(ind-3, dp)
            return dp[ind]
        
        return get_tribo(n, dp)

# LC hard
# Link: https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        def subseq(si, ti):
            # safety
            if si > n or ti > m:
                return 0
            
            # base case
            if ti == m: # match
                return 1
            if si == n: # no match
                return 0
            
            # memo check
            if dp[si][ti] != -1:
                return dp[si][ti]
            
            # take the char
            take = 0
            if s[si] == t[ti]:
                take = subseq(si+1, ti+1)
            
            # skip the char
            skip = subseq(si+1, ti+0)
            
            dp[si][ti] = take + skip
            return dp[si][ti]
        
        return subseq(0, 0)

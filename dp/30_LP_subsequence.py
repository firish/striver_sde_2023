# Link: 

# Same as LCS, where s2 = s1[::-1
# Memo
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        s2 = s[::-1]
        def lcs(ind1, ind2, dp):
            if ind1 < 0 or ind2 < 0:
                return 0
            
            # memo
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            # match
            match, not_match = 0, 0
            if s[ind1] == s2[ind2]:
                match = 1 + lcs(ind1-1, ind2-1, dp)
            # not match
            else:
                not_match = 0 + max(lcs(ind1-1, ind2, dp), lcs(ind1, ind2-1, dp))
            
            dp[ind1][ind2] = max(match, not_match)
            return dp[ind1][ind2]
        
        dp = [[-1 for _ in range(len(s2))] for _ in range(len(s))]
        return lcs(len(s)-1, len(s2)-1, dp)

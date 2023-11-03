# Link: https://leetcode.com/problems/longest-common-subsequence/


# Memo solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def lcs(ind1, ind2, dp):
            if ind1 < 0 or ind2 < 0:
                return 0
            if ind1 == 0 and ind2 == 0:
                return 1 if text1[ind1] == text2[ind2] else 0
            
            # memo
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            # match
            match, not_match = 0, 0
            if text1[ind1] == text2[ind2]:
                match = 1 + lcs(ind1-1, ind2-1, dp)
            # not match
            else:
                not_match = 0 + max(lcs(ind1-1, ind2, dp), lcs(ind1, ind2-1, dp))
            
            dp[ind1][ind2] = max(match, not_match)
            return dp[ind1][ind2]
        
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return lcs(len(text1)-1, len(text2)-1, dp)

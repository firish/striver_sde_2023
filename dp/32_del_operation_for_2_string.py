# Link: https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1, s2 = word1, word2
        def lcs(ind1, ind2, dp):
            if ind1 < 0 or ind2 < 0:
                return 0
            
            # memo
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            # match
            match, not_match = 0, 0
            if s1[ind1] == s2[ind2]:
                match = 1 + lcs(ind1-1, ind2-1, dp)
            # not match
            else:
                not_match = 0 + max(lcs(ind1-1, ind2, dp), lcs(ind1, ind2-1, dp))
            
            dp[ind1][ind2] = max(match, not_match)
            return dp[ind1][ind2]
        
        dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
        lcs_val = lcs(len(s1)-1, len(s2)-1, dp)
        
        if lcs_val == len(word1):
            return len(s2) - lcs_val
        elif lcs_val == len(word2):
            return len(s1) - lcs_val
        else:
            return len(s1) + len(s2) - 2*lcs_val

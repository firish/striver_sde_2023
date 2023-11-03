# Link: https://leetcode.com/problems/longest-common-subsequence/


# Memo solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def lcs(ind1, ind2, dp):
            if ind1 < 0 or ind2 < 0:
                return 0
            
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


# tabulation
# has the shifted-index trick
dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for ind2 in range(len(text2)+1):
            dp[0][ind2] = 0
        for ind1 in range(len(text1)+1):
            dp[ind1][0] = 0
        
        for ind1 in range(1, len(text1)+1):
            for ind2 in range(1, len(text2)+1):
                if text1[ind1-1] == text2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1-1][ind2], dp[ind1][ind2-1])
        return dp[len(text1)][len(text2)]


# cleaner tabulation
n1 = len(str1)
n2 = len(str2)

dp = [[0 for j in range(n2+1)] for i in range(n1+1)]

for i in range(1,n1+1):
    for j in range(1,n2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = 1+ dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

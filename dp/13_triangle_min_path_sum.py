# Link: https://leetcode.com/problems/triangle/submissions/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        
        def triang(l, ind, triangle, dp):
            if l == len(triangle)-1:
                return triangle[l][ind]
            
            if dp[l][ind] != 10**12:
                return dp[l][ind]
            
            one, two = 10**12, 10**12
            if ind <= len(triangle[l+1])-1:
                one = triangle[l][ind] + triang(l+1, ind, triangle, dp)
            if ind+1 <= len(triangle[l+1])-1:
                two = triangle[l][ind] + triang(l+1, ind+1, triangle, dp)
            
            dp[l][ind] = min(one, two)
            return dp[l][ind]
        
        dp = []
        for l in range(len(triangle)):
            dp.append([10**12]*len(triangle[l]))
        
        triang(0, 0, triangle, dp)
        return dp[0][0]

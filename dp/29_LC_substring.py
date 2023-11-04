# Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/


# ez in tabulation
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
	
        for ind1 in range(1, len(nums1)+1):
            for ind2 in range(1, len(nums2)+1):
                if nums1[ind1-1] == nums2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = 0
        
        maxi = 0
        for row in dp:
            maxi = max(maxi, max(row))
        return maxi

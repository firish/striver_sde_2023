# Link: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def lis(ind, prev_ind, dp):
            if ind >= len(nums):
                return 0
            
            if dp[ind][prev_ind+1] != -1:
                return dp[ind][prev_ind+1]
            
            take, not_take = 0, 0
            not_take = 0 + lis(ind+1, prev_ind, dp)
            if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                take = 1 + lis(ind+1, ind, dp)
            
            dp[ind][prev_ind+1] = max(take, not_take)
            return dp[ind][prev_ind+1]
        
        dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        return lis(0, -1, dp)



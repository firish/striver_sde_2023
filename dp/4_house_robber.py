# Link: https://leetcode.com/problems/house-robber/submissions/
# Explanation: https://www.youtube.com/watch?v=GrMBfJNk_NY

# My code
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def get_max_sum(nums, ind, dp):
            if ind < 0: 
                return 0
            if ind == 0:
                return nums[0]
            
            # Memoization check DP
            if dp[ind] != -1:
                return dp[ind]
            
            # all operations at the current index
            # 1) pick element
            pick = nums[ind] + get_max_sum(nums, ind - 2, dp)
            
            # 2) Not pick
            skip = 0 + get_max_sum(nums, ind - 1, dp)
            
            # Memoize
            dp[ind] = max(pick, skip)
            return dp[ind]
        
        dp = [-1]*len(nums)
        return get_max_sum(nums, len(nums)-1, dp)
            

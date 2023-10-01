# Link: https://leetcode.com/problems/house-robber-ii/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
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
        
        
        # answer cant contain first and last together
        # skip last element
        dp = [-1]*len(nums)
        no_last = get_max_sum(nums, len(nums)-2, dp) 
        
        # skip first element
        # we go to len(nums)-2 as len of arr has reduced by 1
        dp = [-1]*len(nums)
        no_first = get_max_sum(nums[1:], len(nums)-2, dp) 
        
        return max(no_last, no_first) 

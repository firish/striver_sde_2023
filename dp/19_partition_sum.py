# Link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # array should have two equal subsets
        # therefore subset1 = subset 2
        # thefore if sum of array is s, each subset is s/2
        s = sum(nums)
        if s%2 != 0:return False
        
        # now if we find one subst that is s/2,
        # then the other elements will also total to s/2
        # hence we can return True
        def partition(ind, target, dp):
            # base conditions
            if target < 0:
                return False
            if target == 0:
                return True
            if ind == 0:
                return nums[0] == target
            
            # memo check
            if dp[ind][target] != -1:
                return dp[ind][target]
            
            # take and skip the current ind
            take = partition(ind-1, target-nums[ind], dp)
            skip = partition(ind-1, target, dp)
            
            dp[ind][target] = take or skip
            return dp[ind][target]
        
        # Make the dp array
        # two recursive states, so we need a 2D array
        # each element will be a boolean
        # dp[ind][target] is true if we can,
        # sum elements from index 0 to ind to make the target
        dp = [[-1 for col in range(0, (s//2)+1)] for row in range(0, len(nums))]
        return partition(len(nums)-1, s//2, dp)

# Link: https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        def find(ind, curr, dp):
            if ind == n:
                if curr == target:
                    return 1
                return 0
            
            # memo check
            if (ind, curr) in dp:
                return dp[(ind, curr)]
            
            # append a positive sign
            pos = find(ind+1, curr + nums[ind], dp)
            
            # append a negative sign
            neg = find(ind+1, curr - nums[ind], dp)
            
            # memoize solution
            dp[(ind, curr)] = pos + neg
            return dp[(ind, curr)]
        
        # some problems are more suited to tabulation
        # Like this one, where you have a 2D grid
        # where dp[i][j] represents the number of ways 
        # to reach sum j using the first i numbers.
        # For memoizing such solutions, 
        # we can use a dict based dp structure
        dp = {}
        return find(0, 0, dp)

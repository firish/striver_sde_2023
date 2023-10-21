# Link: https://leetcode.com/problems/target-sum/
# rec pattern: 1

# Solution (recursion)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def find(ind, curr, res):
            if ind == n:
                if curr == target:
                    res[0] += 1
                return
            
            # append a positive sign
            find(ind+1, curr + nums[ind], res)
            
            # append a negative sign
            find(ind+1, curr - nums[ind], res)
        
        n = len(nums)
        res = [0]
        find(0, 0, res)
        return res[0]

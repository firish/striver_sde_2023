# Link:


# My solution

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        l = len(nums) // 2
        total = sum(nums)
        mini = [10**12]
        
        def min_diff(ind, curr, n):
            # base case
            if n == l:
                s1, s2 = curr, total - curr
                diff = abs(s1 - s2)
                if diff < mini[0]:
                    mini[0] = diff
                return
            if ind >= len(nums):
                return
            
            # Check if result is already computed
            if (ind, curr, n) in dp:
                return
            
            # take and skip
            min_diff(ind + 1, curr + nums[ind], n + 1)
            min_diff(ind + 1, curr, n)
            
            # Store result in dp 
            # in this case, we don't have a return value to store, but the memoization structure is set up
            # We will simply skip that sub-problem in the future
            dp[(ind, curr, n)] = None
            return
        
        dp = {}
        min_diff(0, 0, 0)
        return mini[0]


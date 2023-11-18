# Problem link: https://leetcode.com/problems/next-greater-element-ii/submissions/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # copy the same array to right
        # Then solve similarly to next greater element 1
        # this takes care of the circular indexing problem
        nums = nums + nums
        n = len(nums)
        
        mis = []
        next_greater = [-1]*n
        for i, num in enumerate(nums[::-1]):
            
            ind = n - i - 1
            while len(mis) > 0 and num >= mis[-1]:
                mis.pop()
            
            if len(mis) > 0 and num != mis[-1]:
                next_greater[ind] = mis[-1]
            
            mis.append(num)
        
        return next_greater[:n//2:1]
        
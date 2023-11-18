# problem Link: https://leetcode.com/problems/next-greater-element-i/submissions/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # create an index map (not required for MIS)
        index_map = {}
        
        # for the next greater element, 
        # traverse right to left
        # and use a monotonically increasing stack
        n = len(nums2)
        mono_inc_stack = []
        next_greater = [-1]*n
        for i, num in enumerate(nums2[::-1]):
            ind = n-i-1
            index_map[num] = ind
            # if stack has elements, pop until the top of stack has next greater
            while len(mono_inc_stack) > 0 and num > mono_inc_stack[-1]:
                mono_inc_stack.pop()
            
            # after poping, if stack still has elements, next greater element exists
            if len(mono_inc_stack) > 0:
                next_greater[ind] = mono_inc_stack[-1]
            
            # at the end, always add current element to top of stack
            mono_inc_stack.append(num)
        
        res = []
        for num in nums1:
            if num in index_map:
                res.append(next_greater[index_map[num]])
        return res
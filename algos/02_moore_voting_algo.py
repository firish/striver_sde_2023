# Link: https://leetcode.com/problems/majority-element/submissions/

# For finding majority element of an array
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Moore Voting Algorithm
        # Solve the question in O(1) space
        
        # Intuition
        # if an element is the majority element (freq(el) >= n / 2)
        # any other element can not be the majority element
        
        # simple keep an element var and a count
        # when you see the same element, inc count, else decrease it by 1
        # every time freq dips below 0, change the element
        
        element = nums[0]
        freq = 1
        for el in nums[1:]:
            if el == element:
                freq += 1
            else:
                freq -= 1
                if freq < 0:
                    element = el
                    freq = 0
        return element

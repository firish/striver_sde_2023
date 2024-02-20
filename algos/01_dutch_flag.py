# Link: https://leetcode.com/problems/sort-colors/discuss/4754877/Python-using-the-Dutch-Flag-Algo

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch flag algo
        # sort three numbers, asc, or desc
        # time -> O(1), space -> O(N)

        # intuition -> use three pointers
        # one for low number, one for high number, one for traversing the arr
        
        # handles list smaller than n=3
        if len(nums) <= 1:
            return nums

        low_pointer, curr, high_pointer = 0, 0, len(nums)-1       
        while curr < len(nums):    
            # skip ones
            if nums[curr] == 1: 
                curr += 1
            # swap 0's at low and 2's at high
            elif nums[curr] == 0:
                nums[low_pointer], nums[curr] = nums[curr], nums[low_pointer]
                low_pointer += 1
            else:
                nums[high_pointer], nums[curr] = nums[curr], nums[high_pointer]
                high_pointer -= 1
            
            if low_pointer > curr:
                curr += 1
            if high_pointer < curr:
                break

        return nums
            

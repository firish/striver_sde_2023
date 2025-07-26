# LC 4 (Hard)
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/

class Solution:
    # The trick: 
    # We don't need to actually sort the array.
    # If the arrays are [1,4,7,8] and [2,3,5,6]
    # You don't need [1,2,3,4,5,6,7,8] to find the median.
    # Combinations like [3,2,1,4,8,6,5,7] or [1,3,2,4,8,7,5,6] and many others also work, as we just need the median.
    # we just need to make sure that 
    # 1. left half has smaller elements than right half
    # 2. biggest element in left half is the last element of left half
    # 3. smallest element in right half is the first element of right half

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Intuition
        # If you cut that combined array exactly in half (left half has n//2 elements).
        # Do a binary search only on the shorter array, you get a middle index.
        # Everything from 0 to middle index of nums1 will count towards the left half of combined array.
        # therefore you also know how many elements must come from nums2 to complete the left half
        # The cut is correct when the largest element on the left side the one array is ≤ the smallest element on the right side of the other.
        # Once that’s true, the median is just the middle element (odd length) or the average of the two straddling elements (even length).

        # Make nums1 the smaller list
        # We do binary search on this list, and hence want to pick the smaller list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get the total length and length of the left half of combined list
        combined_list_length = len(nums1) + len(nums2)
        combined_list_left_half_length = combined_list_length // 2

        # Find the median
        left, right = 0, len(nums1) - 1
        while True:
            # Get the the middle index for smaller list
            nums1_middle_index = (left + right) // 2

            # Get the middle index for the bigger list
            nums2_middle_index = combined_list_left_half_length - nums1_middle_index - 2 # -1 to account for 0-indexing of combined_list_left_half and -1 for 0-indexing of nums_1

            # Get the right most value of the two lists going in left half
            nums1_left = nums1[nums1_middle_index] if 0 <= nums1_middle_index else float('-inf')
            nums2_left = nums2[nums2_middle_index] if 0 <= nums2_middle_index else float('-inf')

            # Get the left most value of the two lists going in right half
            nums1_right = nums1[nums1_middle_index + 1] if (nums1_middle_index + 1) < len(nums1) else float('inf')
            nums2_right = nums2[nums2_middle_index + 1] if (nums2_middle_index + 1) < len(nums2) else float('inf')

            # case 1: check if the left partition was correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # case 1.1: total_length is odd
                # the middle element is the last element of left half
                if combined_list_length & 1 == 1:
                    return min(nums1_right, nums2_right)
                # case 1.2: total_length is even
                # the middle element is the average of last element of left half and first element of right half
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            
            # case 2: if partition was incorrect and we have taken more elements from smaller list
            if nums1_left > nums2_right:
                right = nums1_middle_index - 1
            
            # case 3: if partition was incorrect and we have taken less elements from smaller list
            if nums2_left > nums1_right:
                left = nums1_middle_index + 1

# LC Hard - 42
# URL: https://leetcode.com/problems/trapping-rain-water/description/


# My soln

class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if not height:
            return 0
        
        # get max height to left of each node
        left_max = []
        curr_max = height[0]
        for i in range(0, len(height)):
            if i == 0:
                left_max.append(0)
                curr_max = max(curr_max, height[i])
                continue
            else:
                curr_max = max(curr_max, height[i-1])
                left_max.append(curr_max)
        # print(left_max)

        # get max height to right of each node
        right_max = [0]*len(height)
        curr_max = height[-1]
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right_max[i] = 0
                curr_max = max(curr_max, height[i])
                continue
            else:
                curr_max = max(curr_max, height[i+1])
                right_max[i] = curr_max
        # print(right_max)

        rain_water = 0
        for i in range(len(height)):
            max_height = min(left_max[i], right_max[i])
            rain_water += max(0, max_height - height[i])
        return rain_water


# 2-Pointer, single pass optimization
class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if not height:
            return 0

        left, right = 1, len(height)-2
        left_max = height[0]
        right_max = height[-1]
        rain_water = 0
        while left <= right:
            max_height = min(left_max, right_max)
            if left_max <= right_max:
                rain_water += max(0, max_height - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                rain_water += max(0, max_height - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return rain_water

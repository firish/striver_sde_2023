class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        for ind in range(1, len(nums)):
            for prev in range(0, ind):
                if nums[ind] > nums[prev]:
                    dp[ind] = max(dp[ind], 1 + dp[prev])
        
        # to print lis
        lis = max(dp)
        ans = [0]*lis
        for i in range(len(dp)-1, -1, -1):
            if dp[i] == lis:
                ans[lis-1] = nums[i]
                lis -= 1
        print(ans)


# A more stable way of printing the LIS
from collections import deque
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        mapping = [0] * len(nums)
        maxi = 0
        max_ind = 0
        for ind in range(1, len(nums)):
            mapping[ind] = ind
            for prev in range(0, ind):
                if nums[ind] > nums[prev]:
                    if dp[ind] < 1 + dp[prev]:
                        dp[ind] = 1 + dp[prev]
                        mapping[ind] = prev
            if dp[ind] > maxi:
                maxi = dp[ind]
                max_ind = ind
        
        # to print lis
        ans = deque()
        while mapping[max_ind] != max_ind:
            ans.appendleft(nums[max_ind])
            max_ind = mapping[max_ind]
        ans.appendleft(nums[max_ind])
        print(ans)
        return maxi

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

# Code Ninja
# Link: https://www.codingninjas.com/studio/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0

# memo
def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    nums = arr

    def subset(ind, curr, dp):
        if curr < 0:
            return 0
        if curr == 0:
            return 1
        if ind == 0:
            return 1 if nums[0] == curr else 0
        
        # memo check
        if dp[ind][curr] != -1:
            return dp[ind][curr]
        
        # take
        take = subset(ind-1, curr-nums[ind], dp)
        skip = subset(ind-1, curr, dp)
        
        # memo
        dp[ind][curr] = take + skip
        return dp[ind][curr]
        
    dp = [[-1 for _ in range(k+1)] for _ in range(len(nums))]
    return subset(len(nums)-1, k, dp) % (10**9 + 7)


# tabulated

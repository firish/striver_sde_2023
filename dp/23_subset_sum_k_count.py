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
def findWays(arr: List[int], k: int) -> int:
    # Write your code here.

    dp = [[0 for _ in range(k+1)] for _ in range(len(arr))]
    # table setup
    for ind in range(0, len(arr)):
        dp[ind][0] = 1 # ways to make 0
    # base case
    if arr[0] <= k:
        dp[0][arr[0]] = 1 
        
    for ind in range(1, len(arr)):
        for curr in range(1, k+1):
            take, skip = 0, 0
            if curr >= arr[ind]:
                take = dp[ind-1][curr-arr[ind]]
            skip = dp[ind-1][curr]
            dp[ind][curr] = (take + skip) % (10**9 + 7)
    return dp[len(arr)-1][k] 


# my first space-optimized dp (god level)!
    def findWays(arr: List[int], k: int) -> int:
    # Write your code here.

    # space optimized
    dp = [[0 for _ in range(k+1)]]
    
    # table setup
    dp[0][0] = 1 # ways to make 0
    # base case
    if arr[0] <= k:
        dp[0][arr[0]] = 1 
        
    for ind in range(1, len(arr)):
        next_row = [0]*(k+1)
        # if trying space optimization, make sure
        # curr starts from 0 and not 1
        # as 0th index is not taken care of like normal tabulation
        for curr in range(0, k+1): 
            take, skip = 0, 0
            if curr >= arr[ind]:
                take = dp[0][curr-arr[ind]]
            skip = dp[0][curr]
            next_row[curr] = (take + skip) % (10**9 + 7)
        dp[0] = next_row
    return dp[0][k] 

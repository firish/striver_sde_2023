# Not on LC
# Code Ninja problem (level: Hard)
# Link: https://www.codingninjas.com/studio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?leftPanelTab=0

# Solution
# using Tabulation


def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    
    total = sum(arr)
    # This question is very well suited to Tabulation
    dp = [[False for _ in range(total+1)] for _ in range(n)]
    
    # base case
    # you can always get 0
    for ind in range(0, n):
        dp[ind][0] = True
    # its always possible to make the first element
    dp[0][arr[0]] = True

    # Tabulate
    for ind in range(1, n):
        for curr in range(1, total+1):
            # not take
            skip = dp[ind-1][curr]
            # take case
            take = False
            if curr > arr[ind]:
                take = dp[ind-1][curr-arr[ind]]
            dp[ind][curr] = take or skip

    mini = total
    for i, reachable in enumerate(dp[-1]):
        if reachable:
            mini = min(mini, abs(i-(total-i)))

    return mini

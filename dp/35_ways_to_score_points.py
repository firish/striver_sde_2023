points = [1, 2, 3, 4]
n = len(points)
calls = [0]
def get_combs(ind, target, n, points, calls):
    calls[0] += 1
    # base case
    if target < 0:
        return 0
    if ind == -1:
        return 1 if target == 0 else 0
        
    # take the current number as many times as possible
    take = get_combs(ind, target-points[ind], n, points, calls)
    skip = get_combs(ind-1, target, n, points, calls)
    return take + skip

print(get_combs(n-1, 117, n, points, calls)*get_combs(n-1, 120, n, points, calls))
print(calls)
    
# 170868600
# [1696550]

# LOOK AT THE DIFF WITH DP!!
points = [1, 2, 3, 4]
n = len(points)
calls = [0]
def get_combs(ind, target, n, points, dp, calls):
    calls[0] += 1
    # base case
    if target < 0:
        return 0
    if ind == -1:
        return 1 if target == 0 else 0
        
    # memo check
    if dp[ind][target] != -1:
        return dp[ind][target]
        
    # take the current number as many times as possible
    take = get_combs(ind, target-points[ind], n, points, dp, calls)
    skip = get_combs(ind-1, target, n, points, dp, calls)
    
    dp[ind][target] = take + skip
    return dp[ind][target]

dp1 = [[-1 for _ in range(118)] for _ in range(n)]
dp2 = [[-1 for _ in range(121)] for _ in range(n)]
print(get_combs(n-1, 117, n, points, dp1, calls)*get_combs(n-1, 120, n, points, dp2, calls))
print(calls)
    
# 170868600
# [1542]

# If you do a tabulation, bottom-up approach
# 170868600
# [711], space = O(4*118) + O(4*120)

# If you do a space-optimized dp, it will reduce to
# [711], space = O(120)

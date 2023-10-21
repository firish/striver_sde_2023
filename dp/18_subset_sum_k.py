# Coding Ninja
# Link: https://www.codingninjas.com/studio/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

# solution
from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    # for subset problems
    # (ind, target) => from 0 to index, can you find target? 
    def check(ind, target, dp):

        # base cases
        if target == 0: return True
        elif arr[ind] == target: return True
        
        if ind == 0:
            if arr[0] == target: return True
            return False
        
        # memo check
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        # two options per index, take it, or skip it
        # taking the index in subset
        take = False
        if target - arr[ind] > 0: # only take if valid
            take = check(ind-1, target-arr[ind], dp)
        
        # skipping the index
        skip = check(ind-1, target, dp)

        # memoize
        dp[ind][target] = take or skip
        return dp[ind][target]
    
    # make the dp array
    # 2 states, index and target, so we need a 2D array
    dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    return check(n-1, k, dp)
    
    
    


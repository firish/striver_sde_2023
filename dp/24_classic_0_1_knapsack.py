# Code Forces
# Problem Link: https://www.codingninjas.com/studio/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1

# Memo
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    wts = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    bag_wt = int(input())

    if n == 1: 
        if bag_wt >= wts[0]: print(vals[0])
        else: print(0)
        continue

    def knapsack(ind, wt, dp):
        if wt == bag_wt:
            return 0
        if ind == 0:
            if bag_wt >= wt + wts[ind]:
                return vals[ind]
            return 0

        # memo check
        if dp[ind][wt] != -1:
            return dp[ind][wt]
        
        # two options
        pick, skip = -10**10, -10**10
        skip = 0 + knapsack(ind-1, wt, dp)
        if bag_wt >= wt + wts[ind]:
            pick = vals[ind] + knapsack(ind-1, wt+wts[ind], dp)

        # memo
        dp[ind][wt] = max(skip, pick)
        return dp[ind][wt]
    
    dp = [[-1 for _ in range(bag_wt+1)] for _ in range(n)]
    print(knapsack(n-1, 0, dp))



# tabulation
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    wts = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    bag_wt = int(input())

    if n == 1: 
        if bag_wt >= wts[0]: print(vals[0])
        else: print(0)
        continue
    
    dp = [[0 for _ in range(bag_wt+1)] for _ in range(n)]
    # base case
    for wt in range(1, bag_wt+1):
        if wts[0] <= wt:
            dp[0][wt] = vals[0]

    for ind in range(1, n):
        for wt in range(1, bag_wt+1):
            skip = dp[ind-1][wt]
            take = -10**10
            if wts[ind] <= wt:
                take = vals[ind] + dp[ind-1][wt-wts[ind]]
            dp[ind][wt] = max(skip, take)
    print(dp[n-1][bag_wt])


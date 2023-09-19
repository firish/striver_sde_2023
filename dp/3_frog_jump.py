# Link: https://www.codingninjas.com/studio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos


from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [-1]*(n)

    def jump(heights, curr, dp):
        if curr == 0:
            return 0
        
        if dp[curr] != -1:
            return dp[curr]
        
        one = jump(heights, curr-1, dp) + abs(heights[curr] - heights[curr-1])  
        
        two = 10**10
        if curr > 1:
            two = jump(heights, curr-2, dp) + abs(heights[curr] - heights[curr-2])
        
        dp[curr] = min(one, two)
        return dp[curr]
    
    return jump(heights, n-1, dp)

# Tabulation
dp = [0]*(n)
    for i in range(1, n):
        one = dp[i-1] + abs(heights[i] - heights[i-1])
        two = 10**10
        if i > 1:
            two = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(one, two)
    return dp[-1]

# Link: https://www.codingninjas.com/studio/problems/ninja-s-training_3621003?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=1

from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    def train(points, ind, prev, dp):
        # stop case
        if ind == 0:
            maxi = 0
            for i in range(0, 3):
                if i != prev:
                    maxi = max(maxi, points[ind][i])
            return maxi
        
        # recursion, try all values
        maxi = 0
        for i in range(0, 3):
            if i != prev:
                # memoization check
                if dp[ind][i] != 0:
                    score = dp[ind][i]
                else:
                    score = points[ind][i] + train(points, ind-1, i, dp)
                    # memoize
                    dp[ind][i] = score
                maxi = max(maxi, score)
        return maxi

    # create dp state
    # Number of days * tasks (0, 1, 2, and 3 or no task)
    dp = [[0]*4 for _ in range(n)]

    return train(points, n-1, 3, dp)
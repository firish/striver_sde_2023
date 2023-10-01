from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Number of days * tasks (0, 1, 2, and 3 or no task)
    dp = [[0]*4 for _ in range(n)]
    # set up base case for tabulation
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    
    # bottom up tabulation
    for day in range(1, n):
        for prev in range(0, 3):
            maxi = 0
            for task in range(0, 3):
                if task != prev:
                    score = points[day][task] + dp[day-1][task]
                    maxi = max(maxi, score)
            dp[day][prev] = maxi
    return max(dp[-1])

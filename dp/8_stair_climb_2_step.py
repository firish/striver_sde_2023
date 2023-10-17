# Link: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        dp = [10**12]*len(cost)
        def get_cost(ind, cost, dp):
            if ind == 0:
                return cost[0]
            if ind < 0:
                return 0
            
            if dp[ind] != 10**12:
                return dp[ind]
                
            one = cost[ind] + get_cost(ind-1, cost, dp)
            two = cost[ind] + get_cost(ind-2, cost, dp)
            dp[ind] = min(one, two)
            return dp[ind]
        
        get_cost(len(cost)-1, cost, dp)
        return min(dp[-1], dp[-2])

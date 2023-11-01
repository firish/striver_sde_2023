# Link: https://leetcode.com/problems/coin-change-ii/submissions/

# memo
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def coin_change(ind, curr):
            if curr < 0:
                return 0
            if curr == 0:
                return 1
            if ind == 0:
                if curr % coins[ind] == 0: return 1
                return 0
            
            if dp[ind][curr] != -1:
                return dp[ind][curr]
            
            same_coin = coin_change(ind, curr-coins[ind])
            next_coin = coin_change(ind-1, curr)
            
            dp[ind][curr] = same_coin + next_coin
            return dp[ind][curr]
        
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        return coin_change(len(coins)-1, amount)


# tabulation
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        # base case
        for ind in range(len(coins)):
            dp[ind][0] = 1
        for amt in range(amount+1):
            if amt % coins[0] == 0:
                dp[0][amt] = 1
        
        # tabulation
        for ind in range(1, len(coins)):
            for amt in range(1, amount+1):
                same, nxt = 0, 0
                if amt >= coins[ind]:
                    same = dp[ind][amt-coins[ind]]
                nxt = dp[ind-1][amt]
                dp[ind][amt] = same+nxt
        
        return dp[len(coins)-1][amount]

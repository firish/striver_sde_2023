# Link: https://leetcode.com/problems/coin-change/submissions/


# memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def change(ind, curr, dp):
            if ind >= len(coins):
                return 10**12
            if curr > amount:
                return 10**12
            if curr == amount:
                return 0
            
            # memo check
            if dp[ind][curr] != 10**12:
                return dp[ind][curr]
            
            # keep taking current coin till you can
            same = 1 + change(ind, curr+coins[ind], dp)
            # move to the next coin
            diff = 0 + change(ind+1, curr, dp)
            
            # memoize
            dp[ind][curr] = min(same, diff)
            return dp[ind][curr]



# memo with a better base case that doesnt give TLE
        class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def change(ind, curr, dp):
            if curr < 0 or ind < 0:
                return 10**12
            if ind == 0:
                if curr % coins[ind] == 0:
                    return curr / coins[ind]
                return 10**12
            
            # memo check
            if dp[ind][curr] != -1:
                return dp[ind][curr]
            
            # keep taking current coin till you can
            same = 1 + change(ind, curr-coins[ind], dp)
            # move to the next coin
            diff = 0 + change(ind-1, curr, dp)
            
            # memoize
            dp[ind][curr] = min(same, diff)
            return dp[ind][curr]
        

        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        
        res = change(len(coins)-1, amount, dp)
        return int(res) if res != 10**12 else -1



# Tabulating
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create dp array
        # dp[ind][curr], here dp[3][7] has the minimum number of coins
        # that are needed to form the number 7, using the first three coin denominations
        dp = [[10**12 for _ in range(amount+1)] for _ in range(len(coins))]
        
        # base case
        # for the first coin denomination, 
        # store the number of coins of needed to form each target (number)
        for curr in range(amount+1):
            dp[0][curr] = 10**12 # cant form
            if curr % coins[0] == 0:
                dp[0][curr] = int(curr / coins[0]) # if you can form
        
        # tabulate
        for ind in range(1, len(coins)):
            for curr in range(1, amount+1):
                same_coin = 10**12
                if curr >= coins[ind]:
                    same = 1 + dp[ind][curr-coins[ind]]
                next_coin = 0 + dp[ind-1][curr]
                dp[ind][curr] = min(same_coin, next_coin)
        
        # answer -> minimum coins required to make amount, using all available coin demoniations
        return dp[len(coins)-1][amount]

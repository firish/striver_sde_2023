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

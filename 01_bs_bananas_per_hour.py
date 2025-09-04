# LC 875 (Medium)
#URL: https://leetcode.com/problems/koko-eating-bananas/description/

# My Soln:

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # evaluator
        def hours_needed_to_eat_bananas(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return 1 if hours <= h else 0
        
        # get low and max
        piles.sort()
        low, high = float('inf'), float('-inf')
        for pile in piles:
            high = max(high, pile)
        low = 1
        # print(low, high)

        # binary search go brrr
        slow = float('inf')
        while low <= high:
            k = (low + high) // 2
            res = hours_needed_to_eat_bananas(k)
            if res:
                slow = min(slow, k)
            # print(res)
            
            if res:
                high = k - 1
            else:
                low = k + 1
        
        return slow
            

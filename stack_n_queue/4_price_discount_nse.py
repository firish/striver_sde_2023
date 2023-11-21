# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/submissions/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # we need to find the next smaller element for each index
        # so we can use a monotnic decreasing stack
        n = len(prices)
        mds = [0]*n
        next_smaller = [-1]*n
        for i, num in enumerate(prices[::-1]):
            ind = n-i-1
            while len(mds) > 0 and num < mds[-1]:
                mds.pop()
            if len(mds) > 0:
                next_smaller[ind] = mds[-1]
            mds.append(num)
        
        for i in range(n):
            prices[i] -= next_smaller[i]
        return prices

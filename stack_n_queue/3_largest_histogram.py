# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# LC Hard

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # intuition
        # for every index, the largest possible histogram is 
        # from the prev smaller index to the next smaller index
        # so we use a monotonic increasing stack and a monotonic decreasing stack
        
        # first, to get index of next smaller element at each index
        # we use a mds
        n = len(heights)
        mds_next_smaller  = []
        next_smaller = [n]*n
        for i, num in enumerate(heights[::-1]):
            ind = n - i - 1
            while len(mds_next_smaller) > 0 and num <= mds_next_smaller[-1][1]:
                mds_next_smaller.pop()
            if len(mds_next_smaller) > 0:
                next_smaller[ind] = mds_next_smaller[-1][0]
            mds_next_smaller.append((ind, num))
        
        # second, to get index of prev smallest element at each index
        # we use a mis
        mis_prev_smaller = []
        prev_smaller = [-1]*n
        for i, num in enumerate(heights[::1]):
            ind = i
            while len(mis_prev_smaller) > 0 and num <= mis_prev_smaller[-1][1]:
                mis_prev_smaller.pop()
            if len(mis_prev_smaller) > 0:
                prev_smaller[ind] = mis_prev_smaller[-1][0]
            mis_prev_smaller.append((ind, num))

        # now, get the max histogram area
        maxi = 0
        for i in range(len(heights)):
            width =  next_smaller[i] - prev_smaller[i] - 1
            maxi = max(maxi, width*heights[i])
        return maxi

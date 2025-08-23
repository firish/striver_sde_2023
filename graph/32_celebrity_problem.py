# LC 277 (Medium) (Premium)
# Find Celebrity Problem
# URL: https://leetcode.com/problems/find-the-celebrity/

# My Soln:
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        potential_celebrities = set([i for i in range(n)])
        i, j = 0, 1
        while j < n:
            edge_found = knows(j, i)
            # if true, j is not a celeb
            # remove it from celeb list, and move j ahead
            if edge_found:
                potential_celebrities.remove(j)
            # if fasle, i in not a celeb
            else:
                potential_celebrities.remove(i)
                i = j
            j += 1

        # we should have at most 1 celebrity left
        celebrity = list(potential_celebrities)[0]
        for i in range(n):
            if (i != celebrity) and (knows(celebrity, i) or (not knows(i, celebrity))):
                return -1
        return celebrity
        
        

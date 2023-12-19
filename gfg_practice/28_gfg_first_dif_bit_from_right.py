# Link: https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        x = bin(m)[2:]
        y = bin(n)[2:]
        if x == y:
            return -1
        # print(x, y)
        xl, yl = len(x), len(y)
        for i in range(min(xl, yl)):
            if x[xl-1-i] == y[yl-1-i]:
                continue
            return i+1
        if xl < yl:
            return xl + 1
        else:
            return yl + 1

#User function Template for python3
import math

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        ind = sizeOfStack - math.ceil((sizeOfStack+1)/2)
        return s.pop(ind)

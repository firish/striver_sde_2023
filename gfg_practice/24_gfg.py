# find Link at: https://practice.geeksforgeeks.org/problems/reverse-a-stack/1

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        i, j = 0, len(St)-1
        while i < j:
            St[i], St[j] = St[j], St[i]
            i += 1; j-= 1
        return

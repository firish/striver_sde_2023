link: https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1

from collections import defaultdict
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        res = '$'
        for char in s:
            if freq[char] == 1:
                return char
        return res
    
        # alternate
        for x in s:
                if s.count(x) == 1:
                   return x
                 
            return "$"

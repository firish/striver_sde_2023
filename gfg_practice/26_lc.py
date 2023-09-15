# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
		# store latest index of all chars in the string
        pos = defaultdict(int)
        start = 0
        maxi = 0

        for idx in range(len(s)):
			# if you find a repeating index, move the start position ahead
			# the max func is used to ensure that you don't move the start behind its current value (it should only move ahead)
            if s[idx] in pos:
                start = max(start, pos[s[idx]]+1)
            pos[s[idx]] = idx
            maxi = max(maxi, idx-start+1) 
        
        return maxi

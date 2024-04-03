# Link: https://leetcode.com/problems/longest-nice-substring/submissions/

from collections import defaultdict 
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) <= 1: 
            return ""
        
        else:
            tmp_set = set(s)
            for j in range(len(s)):
                
                if s[j].upper() in tmp_set and s[j].lower() in tmp_set:
                    continue
                else:
                    left = self.longestNiceSubstring(s[0:j])
                    right = self.longestNiceSubstring(s[j+1:])
                    if len(left) >= len(right):
                        return left
                    return right
            
            return s

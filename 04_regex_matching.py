# LC 10 (HARD)
# URL: https://leetcode.com/problems/regular-expression-matching/

# My Soln
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def match_regex(s_ind, p_ind):
            # break 1: strings are equal
            if s_ind >= len(s) and p_ind >= len(p):
                return True
            # break 2: p is over, but s is left
            if s_ind < len(s) and p_ind >= len(p):
                return False
            
            # Check if the current chars match
            is_current_match = s_ind < len(s) and (p[p_ind] == s[s_ind] or p[p_ind] == '.')

            # String Matching - '*'
            if p_ind + 1 < len(p) and p[p_ind+1] == '*':
                take_star = is_current_match and match_regex(s_ind+1, p_ind)     # use star and try matching next char
                no_star = match_regex(s_ind, p_ind+2)       # don't use star and move to next char in p
                return (take_star or no_star)

            # String Matching - Char or '.'
            elif s_ind < len(s) and p_ind < len(p) and is_current_match:
                return match_regex(s_ind+1, p_ind+1)
            
            # String doesnt match, return False
            return False
        
        return match_regex(0, 0)

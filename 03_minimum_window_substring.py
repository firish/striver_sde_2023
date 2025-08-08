# LC 76 (Hard)
# URL: https://leetcode.com/problems/minimum-window-substring/

# My Solution
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = defaultdict(int)
        needed_total = 0
        for char in t:
            if char not in needed:
                needed_total += 1
            needed[char] += 1

        adder, popper = 0,0
        having = defaultdict(int)
        having_total = 0
        min_len = float('inf')
        res = -1
        while adder < len(s):
            # Keep Adding
            while adder < len(s) and having_total != needed_total:
                char = s[adder]
                having[char] += 1
                if having[char] == needed[char]:
                    having_total += 1
                adder += 1
            
            # check if current window is minimum
            if having_total == needed_total and adder - popper < min_len:
                min_len = adder - popper
                res = popper
            
            # keep popping
            while popper < adder and having_total == needed_total:
                char = s[popper]
                having[char] -= 1
                if needed[char] > 0 and having[char] < needed[char]:
                    having_total -= 1
                popper += 1

                if having_total == needed_total and adder - popper < min_len:
                    min_len = adder - popper
                    res = popper
            
        return s[res:res+min_len] if min_len != float('inf') else ""
                    

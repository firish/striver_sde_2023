# Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/discuss/4499301/Python-simple-O(N)-solution

from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = []
        for row in bank:
            if any(int(col)==1 for col in row):
                x = Counter(row)
                beams.append(x['1'])
        
        res = 0
        for i in range(1, len(beams)):
            res += beams[i]*beams[i-1]
        return res

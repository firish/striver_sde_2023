#User function Template for python3
from collections import defaultdict
class Solution:
    def FirstNonRepeating(self, A):
        freq = defaultdict(int)
        res = []
        first = []
        for el in A:
            if freq[el] == 0:
                if len(first) == 0:
                    res.append(el)
                else:
                    res.append(first[0])
                first.append(el)
                freq[el] += 1
            else:
                if freq[el] <= 1:
                    first.remove(el)
                freq[el] += 1
                if len(first) == 0:
                    res.append('#')
                else:
                    res.append(first[0])
        return ''.join(res)
                    

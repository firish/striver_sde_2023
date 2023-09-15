# Link: https://leetcode.com/problems/group-anagrams/


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            h[key].append(s)
        return list(h.values())

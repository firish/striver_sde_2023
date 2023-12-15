# Link: https://leetcode.com/problems/destination-city/

from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outdegrees = defaultdict(int)
        cities = set()
        for src, dest in paths:
            outdegrees[src] += 1
            cities.add(src)
            cities.add(dest)
        
        for city in cities:
            if outdegrees[city] < 1:
                return city
        return ""

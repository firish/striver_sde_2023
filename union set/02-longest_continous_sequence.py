# LC 128 Medium
# Disjoint Set
# URL: https://leetcode.com/problems/longest-consecutive-sequence/

# Solution
from collections import defaultdict

class DisjointSet:

    def __init__(self, n):
        self.size = [1]*n
        self.parent = [num for num in range(0, n)]

    # To find the ultimae parent
    def find_parent(self, node):
        # base case
        # when a node is its own parent
        if node == self.parent[node]:
            return node

        # path compression
        pn = self.find_parent(self.parent[node])
        self.parent[node] = pn
        
        # return the parent
        return pn


    # Grow the disjoint set
    def union(self, u, v):
        # find the ultimate parents
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        
        # If they are already in the same set, do nothing
        if pu == pv:
            return
        
        # Always connect the lower rank to the higher rank
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

    # check if two nodes are joint or disjoint
    def are_connected(self, u, v):
        return self.find_parent(u) == self.find_parent(v)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        
        # only keep unique numbers
        unique_nums = set(nums)
        
        # create a hash map to map all unique nums to a unique index
        mappings = defaultdict(int)
        for ind, num in enumerate(unique_nums):
            mappings[num] = ind
        
        # create a disjoint set
        ds = DisjointSet(len(mappings))
        
        # for concecutive numbers - connect
        for num in unique_nums:
            if num+1 in mappings:
                ds.union(mappings[num], mappings[num+1])
        
        # return the component with the largest size
        maxi = 1
        for num in unique_nums:
            component_parent_mapping = ds.find_parent(mappings[num])
            component_size = ds.size[component_parent_mapping]
            maxi = max(maxi, component_size)
        return maxi
        
        

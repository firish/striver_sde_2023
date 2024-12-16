# LC 2316
# count unreachable nodes in an undirected graph
# LC Medium
# DSU

# URL: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# My solution
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        ds = DisjointSet(n)
        for edge in edges:
            u, v = edge[0], edge[1]
            ds.union(u, v)
        
        # traverse - path compression
        for node in range(n):
            ds.find_parent(node)
        # print(ds.parent, ds.size)
        
        cluster_size = {}
        for node in range(n):
            if ds.parent[node] not in cluster_size:
                cluster_size[ds.parent[node]] = ds.size[ds.parent[node]]
        # print(cluster_size)
        
        # you can use a nested for loop to get all pairs
        # or use the formula:
        # ((sum of all cluster sizes)**2 - (sum of the squares of each cluster size)**2 )/2
        # why does it work:
        # The total number of unordered pairs from all nodes s = S*(S-1) / 2
        # Subtract Pairs Within the Same Cluster sc
        # so, sum of the squares of each cluster size
        s, sc = 0, 0
        for k, v in cluster_size.items():
            s += v
            sc += v**2
        return ((s**2) - sc) // 2 # /2 cause pairs
            

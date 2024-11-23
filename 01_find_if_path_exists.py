# Union Finding - Rank
# LC 1971
# URL: https://leetcode.com/problems/find-if-path-exists-in-graph/


# using Rank
class DisjointSet:

    def __init__(self, n):
        self.rank = [0]*n
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
        
        # Always connect the lower rank to the higher rank
        if self.rank[pu] >= self.rank[pv]:
            self.rank[pu] += 1
            self.parent[pv] = pu
        else:
            self.rank[pv] += 1
            self.parent[pu] = pv

    # check if two nodes are joint or disjoint
    def are_connected(self, u, v):
        return self.find_parent(u) == self.find_parent(v)

    
class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # create the disjoint set
        ds = DisjointSet(n)
        for edge in edges:
            ds.union(edge[0], edge[1])
        
        # print(ds.rank)
        # print(ds.parent)
        return ds.are_connected(source, destination)

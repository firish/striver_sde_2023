# LC 959: https://leetcode.com/problems/regions-cut-by-slashes/
# LC Hard

# DSU

# URL: https://leetcode.com/problems/regions-cut-by-slashes/


from collections import defaultdict

# Also tracks cycles - simple change
class DisjointSet:

    def __init__(self, n):
        self.size = [1]*n
        self.parent = [num for num in range(0, n)]
        self.cycle_count = 0 

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
            self.cycle_count += 1
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
    
    def get_edges(self, symbol, r, c, mapping):
        # print(symbol, r, c)
        if symbol == " ":
            return (-1, -1)
        if symbol == "/":
            return (mapping[(r, c+1)], mapping[(r+1, c)])
        if symbol == "\\":
            return (mapping[(r, c)], mapping[(r+1, c+1)])
    
    
    def regionsBySlashes(self, grid: List[str]) -> int:
        # create mapping
        n = len(grid)
        rows, cols = n+1, n+1
        mapping = defaultdict(int)
        ind = 1
        for row in range(0, rows, 1):
            for col in range(0, cols, 1):
                mapping[(row, col)] = ind
                ind += 1
        
        # create DSU
        ds = DisjointSet(rows*cols + 1)
        
        # connect the grid (horizontal and vertical boundaries)
        for r in range(rows-1):
            ds.union(mapping[(r, 0)], mapping[(r+1, 0)])
            ds.union(mapping[(r, n)], mapping[(r+1, n)])
        for c in range(cols-1):
            ds.union(mapping[(0, c)], mapping[(0, c+1)])
            ds.union(mapping[(n, c)], mapping[(n, c+1)])
        
        # create edge list and connect edges
        edges = []
        for row_ind, row in enumerate(grid):
            for symb_ind, symbol in enumerate(row):
                u, v = self.get_edges(symbol, row_ind, symb_ind, mapping)
                if u != -1:
                    ds.union(u, v)
                    
        return ds.cycle_count
                    

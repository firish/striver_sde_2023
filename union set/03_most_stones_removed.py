# LC Medium 947 - Most stones Unturned
# Disjoint Set

# URL: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

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
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # build graph (adjacency lists)
        row_al = defaultdict(list)
        col_al = defaultdict(list)
        mapping = defaultdict(int)
        for i, stone in enumerate(stones):
            x, y = stone[0], stone[1]
            row_al[y].append((x, y))
            col_al[x].append((x, y))
            mapping[(x, y)] = i
        
        # build disjoint set
        ds = DisjointSet(len(stones))
        
        # connect stones by row
        for k, val_list in row_al.items():
            l = len(val_list)
            if l <= 1: 
                continue
            for i in range(0, l-1):
                u, v = val_list[i], val_list[i+1]
                ds.union(mapping[u], mapping[v])
             
        # connect stones by col
        for k, val_list in col_al.items():
            l = len(val_list)
            if l <= 1: 
                continue
            for i in range(0, l-1):
                u, v = val_list[i], val_list[i+1]
                ds.union(mapping[u], mapping[v])
        
        # update the parent for each node in ds
        for node in range(len(mapping.values())):
            ds.find_parent(node) # make sure ultimate parent is updated via path compression
        
        # get total removable stones
        total = 0
        components = 0
        for parent in set(ds.parent):
            total += ds.size[parent]
            components += 1
            
        return total-components if total-components >= 0 else 0
    

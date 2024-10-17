# Clone Graph
# LC 133
# LC Medium

# URL: https://leetcode.com/problems/clone-graph/

# My solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # to hold all copied nodes
        nodes = [0]*101
        nodes[node.val] = Node(node.val)
        
        # BFS
        q = deque()
        seen = set()
        res = []
        
        q.append(node)
        seen.add(node)
        while len(q) > 0:
            curr = q.pop()
            
            nbrs = []
            for nbr in curr.neighbors:
                if nbr not in seen:
                    q.append(nbr)
                    seen.add(nbr)
                    # also create that node's copy
                    nodes[nbr.val] = Node(nbr.val)
                
                nbrs.append(nodes[nbr.val])
            
            nodes[curr.val].neighbors = nbrs

        return nodes[1]

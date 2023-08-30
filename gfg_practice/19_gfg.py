# Find link at: https://www.geeksforgeeks.org/deque-in-python/

from typing import List
from queue import Queue
from collections import defaultdict
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        g = defaultdict(list)
        for node, edges in enumerate(adj):
            g[node] += edges
        
        # BFS -> using queue
        res = []
        vis = [False for _ in range(V)]
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            res.append(node)
            vis[node] = True
            for edge in g[node]:
                if not vis[edge]:
                    vis[edge] = True
                    q.append(edge)
        return res

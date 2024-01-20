# Shortest Path
# Weighted DAG
# We can use Djikstras as well
# But this is using toposort
# Leetcode prem/ G4G question

# Algorithm
# Make a graph (include edge weight)
# Perform topo and get topo ordering (dfs, or kahns algo)
# traverse in topo ordering and release the edges

from typing import List
from collections import defaultdict, deque
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        indegrees = [0]*n
        graph = defaultdict(list)
        for ui, vi, di in edges:
            graph[ui].append((vi, di))
            indegrees[vi] += 1
        
        # topological
        q = deque()
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append((node))

        topo = []
        while len(q) > 0:
            node = q.popleft()
            for nbr, dist in graph[node]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    q.append(nbr)
            topo.append(node)
        topo = topo[::-1]
        
        # get distance using topo
        dist = [float('inf')]*n
        dist[0] = 0
        while len(topo) > 0:
            curr = topo.pop()
            curr_dist = dist[curr]
            for nbr, nbr_dist in graph[curr]:
                dist[nbr] = min(dist[nbr], curr_dist + nbr_dist)
        
        # op formatting
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist

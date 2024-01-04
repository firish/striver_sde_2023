# Bipartite Graph
# Graph nodes can be colored using two colors in a way such that no two adjacent (connected) nodes have the same color

# Link: https://leetcode.com/submissions/detail/1136448378/

from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # all linear graphs are always bi-partite
        # any graph with even cycle length will also be partite
        # any graph with odd cycle length can NOT be bipartite
        
        color = [-1]*len(graph)
        # using BFS
        q = deque()
        vis = [False]*len(graph)
        for node in range(len(graph)):
            if vis[node]:
                continue
                
            q.append(node)
            color[node] = 'G' # Green
            while q:
                curr = q.popleft()
                vis[curr] = True
                curr_col = color[curr]
                nxt_col = 'G' if curr_col == 'Y' else 'Y'
                for nbr in graph[curr]:
                    if color[nbr] == curr_col:
                        return False
                    if not vis[nbr]:
                        color[nbr] = nxt_col
                        vis[nbr] = True
                        q.append(nbr)
        return True

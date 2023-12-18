# A bit wierd

# Link: https://leetcode.com/problems/redundant-connection/

from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        
        cycles = []
        def dfs(node, parent):
            vis[node] = True
            for nbr in graph[node]:
                if nbr == parent:
                    continue
                elif vis[nbr]:
                    if nbr < node:
                        cycles.append([nbr, node])
                    else:
                        cycles.append([node, nbr])
                    return True
                elif not vis[nbr]:
                    if dfs(nbr, node):
                        return True
            return False
        
        for i in range(len(edges)):
            vis = [False for _ in range(len(edges)+1)]
            res = dfs(i+1, -1)
            
        if len(cycles) == 1:
            return cycles[0]
        else:
            for edge in edges[::-1]:
                if edge in cycles:
                    return edge

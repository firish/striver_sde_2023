# Find safe nodes and terminal nodes

# Link: https://leetcode.com/problems/find-eventual-safe-states/submissions/


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # observations
        # any node that is a part of a cycle will not be a safe node
        # any node connecting to the cycle will not be a safe node
        # all other nodes are be a safe node
        
        vis = [False]*len(graph)
        path_vis = [False]*len(graph)
        safe_nodes = []
        
        def dfs(node):
            vis[node] = True
            path_vis[node] = True
            
            for nbr in graph[node]:
                if not vis[nbr]:
                    if not dfs(nbr):
                        return False
                else:
                    if path_vis[nbr]:
                        return False
            
            path_vis[node] = False
            safe_nodes.append(node)
            return True
        
        for node in range(len(graph)):
            if not vis[node]:
                dfs(node)
        return sorted(safe_nodes)
                
        
        



class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs(g, node, res, vis):
            vis[node] = True
            res.append(node)
            for edge in g[node]:
                if not vis[edge]:
                    dfs(g, edge, res, vis)
        
        res = []
        vis = [False for _ in range(V)]
        dfs(adj, 0, res, vis)
        
        return res

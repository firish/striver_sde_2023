# Link: https://leetcode.com/problems/number-of-provinces/submissions/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # To reword this question,
        # you have to return the number of (directly and indirectly) connected components 
        vis = [False for _ in range(len(isConnected))]
            
        def dfs(node):
            vis[node] = True
            for ind, val in enumerate(isConnected[node]):
                if val == 1 and not vis[ind]:
                    dfs(ind)
            return
        
        provinces = 0
        for node in range(len(isConnected)):
            if not vis[node]:
                dfs(node)
                provinces += 1
          
        return provinces
    

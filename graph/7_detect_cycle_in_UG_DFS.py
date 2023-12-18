# Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph


from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    # Intuition
	    # Here, the vis is to check for the cycle
	    # The only way to go to a node that is not the previous node is if there is cycle
	    
	    # so for the recursive calles also send the parent node
	    # and use the parent to avoid infinite loop
	    # and vis is used for cycle detection
	    
		vis = [False for _ in range(V)]
		def dfs(node, parent):
		    vis[node] = True
		    for nbr in adj[node]:
	            if nbr == parent:
                    continue
                
                if vis[nbr]:
                    return True
                
                if not vis[nbr]:
                    if dfs(nbr, node):
                        return True
                    
		    return False
		                
		    
    		
    	for i in range(V):
    	    if not vis[i]:
    	        res = dfs(i, -1)
    	        if res:
    	            return res
    	return False

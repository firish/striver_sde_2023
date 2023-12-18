# Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph


from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    # Intuition
	    # Here, the vis is to check for the cycle
	    # The only way to go to a node that is not the previous node is if there is cycle
	    
	    # so in the queue also store the previous node in path
	    # and use that to avoid infinite loop
	    # and vis is used for cycle detection
	    
		vis = [False for _ in range(V)]
		def bfs(node):
		    q = deque()
    		q.append((node, -1)) # (curr_node, prev_node)
    		vis[node] = True
    		
    		while q:
    		    node, prev = q.popleft()
    		    for nbr in adj[node]:
    		        if nbr == prev: 
    		            continue
    		        else:
    		            if vis[nbr]:
    		                return True
    		            else:
    		                vis[nbr] = True
    		                q.append((nbr, node))
    		return False
    		
    	for i in range(V):
    	    if not vis[i]:
    	        res = bfs(i)
    	        if res:
    	            return res
    	return False

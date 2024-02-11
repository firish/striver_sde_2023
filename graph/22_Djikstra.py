# Djikstras algo, yay! 
# Remember, don't use a queue. For Djikstra's, always use a PQ. (min-heap) 

# GFG Link:


# My sol,
import heapq
from collections import defaultdict

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        # Create a graph from adj list
        g = defaultdict(list)
        for node, edges in enumerate(adj):
            for edge in edges:
                nbr, dist = edge[0], edge[1]
                g[node].append((nbr, dist))
        
        # Djikstras
        dist_list = [10**12]*V
        dist_list[S] = 0
        
        pq = [((0, S))]
        heapq.heapify(pq)
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            for nbr, dist in g[curr_node]:
                nbr_dist = curr_dist + dist
                if nbr_dist < dist_list[nbr]:
                    dist_list[nbr] = nbr_dist
                    heapq.heappush(pq, (nbr_dist, nbr))
                    
        return dist_list

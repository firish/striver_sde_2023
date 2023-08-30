# find link at: https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1


from typing import List
from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for edge in edges:
            n1, n2, wt = edge[0], edge[1], edge[-1]
            g[n1].append([n2, wt])
        
        distances = [float('inf') for node in range(n)]
        distances[0] = 0
        
        pq = [(0, 0)] #[wt, src]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in g[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return [el if el != float('inf') else -1 for el in distances]

# Link: https://leetcode.com/problems/network-delay-time/discuss/4824819/Python-Djiktras-optimized-using-Set



# optimized using Set
# Intuition:
# With a set, when you add an element
# you can check if it exists in set and remove it
# this costs log.n time but can save time in highly connected graph as you save an iteration of the loop

from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create a graph (DAG)
        g = defaultdict(list)
        for conn in times:
            ui, vi, wi = conn
            g[ui].append((vi, wi))
        
        # Djikstras
        # Using a set
        dist = [10**12]*(n+1)
        dist[k] = 0
        
        s = set()
        s.add((0, k)) # (dist, node)
        while s:
            curr_dist, curr_node = s.pop()
            for edge in g[curr_node]:
                nbr_node, nbr_dist = edge
                nxt_dist = curr_dist + nbr_dist
                if nxt_dist < dist[nbr_node]:
                    prev_dist = dist[nbr_node]
                    dist[nbr_node] = nxt_dist
                    s.add((nxt_dist, nbr_node))
                    # Now remove the same node with previous dist
                    # That is what makes the set implementation worth it
                    if (prev_dist, nbr_node) in s:
                        s.remove((prev_dist, nbr_node))
        
        maxi = 0
        for d in dist[1:]:
            if d == 10**12:
                return -1
            elif d > maxi:
                maxi = d
        return maxi
        

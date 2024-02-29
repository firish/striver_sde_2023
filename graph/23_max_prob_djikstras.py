# Link: https://leetcode.com/problems/path-with-maximum-probability/discuss/4797950/Python-using-Djiktras-with-comments

from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # create a bi-directional weighted graph
        g = defaultdict(list)
        for i, edge in enumerate(edges):
            ui, vi = edge[0], edge[1]
            g[ui].append((vi, succProb[i]))
            g[vi].append((ui, succProb[i]))
        # print(g)
        
        # initialize prob of reaching other nodes as -1, or impossible
        probs = [-1]*n
        # prob of reaching start node is always 1
        probs[start_node] = 1
        heap = []
        # Python only has min_heap, here we need max prob, so we need a max_heap
        # so multiply by -1
        heap.append((-1*1, start_node))
        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            # reconvert values to pos after popping
            curr_prob *= -1
            for edge in g[curr_node]:
                nbr, prob = edge
                # its probability, so here, we multiply
                nxt_prob = curr_prob * prob
                if nxt_prob > probs[nbr] and nbr != start_node:
                    probs[nbr] = nxt_prob
                    # convert back to neg before pushing
                    heapq.heappush(heap, (-1*nxt_prob, nbr))            
        
        # return 0 if it is impossible to reach, else return the max prob
        return probs[end_node] if probs[end_node] != -1 else 0

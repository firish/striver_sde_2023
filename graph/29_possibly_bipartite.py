# LC 886 - Medium
# Possibly Bipartite
# tags: DFS, BFS, Bipartite, Union Find

# URL: https://leetcode.com/problems/possible-bipartition/


from collections import defaultdict

class Solution:
    
    # Solve using DFS with 2 coloring
    def is_bipartite(self, node, paint):
        # color the node and mark it visited
        self.color[node] = paint
        self.visited[node] = True
        
        for nbr in self.gal[node]:
            # Do a DFS is the nbr is uncolored and unvisited 
            if self.color[nbr] == -1 or self.color[nbr] != self.color[node]:
                if not self.visited[nbr]:
                    # color[node] ^ 1 will always be the opp color
                    if not self.is_bipartite(nbr, self.color[node] ^ 1): 
                        return False
            
            # if the nbr has the same color, graph is not bipartite
            else:
                return False

        return True
    
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # Note:
        # A linear graph is always bipartite
        # A cyclic graph with even cycle length can be bipartite
        # A cyclic graph with odd cycle length is NEVER bipartite
        
        # For bipartiteness, always create the graph as an adjacency list
        self.gal = defaultdict(list)
        for dislike in dislikes:
            u, v = dislike[0], dislike[1]
            self.gal[u].append(v)
            self.gal[v].append(u)
        
        self.visited = [False]*(n+1)
        self.color = [-1]*(n+1) # {-1: not colored, 0, and 1 signify the 2 colors}
    
        # check for all connected components
        for node in range(1, n+1):
            if not self.visited[node]:
                if not self.is_bipartite(node, 0):
                    return False

        return True
        

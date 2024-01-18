# Wierdly worded question
# for every node n, answer is the quietset node that is richer/as rich as node i
# Link: https://leetcode.com/problems/loud-and-rich/submissions/

from collections import defaultdict, deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        g = defaultdict(list)
        indegrees = [0]*n
        for rich, poor in richer:
            g[poor].append(rich)
        print(g)
        
        def dfs(node, richer, vis):
            vis[node] = True
            for nbr in g[node]:
                if not vis[nbr]:
                    richer.append(nbr)
                    dfs(nbr, richer, vis)
        
        answer = [-1]*n
        for node in range(n):
            vis = [False]*n
            richer = []
            dfs(node, richer, vis)
            if len(richer) == 0:
                answer[node] = node
            else:
                quietest_node, quiteness = node, quiet[node]
                for richer_node in richer:
                    if quiteness > quiet[richer_node]:
                        quiteness = quiet[richer_node]
                        quietest_node = richer_node
                answer[node] = quietest_node
                
        return answer

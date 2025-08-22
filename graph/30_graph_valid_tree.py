# LC 261 (Medium)
# Graph Valid Tree
# URL: https://leetcode.com/problems/graph-valid-tree/description/

# Solution:
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            g[u].append(v)
            g[v].append(u)

        seen = set()
        def dfs(node, parent):
            for nbr in g[node]:
                if nbr == parent: # skip parent to avoid infinte cycle
                    continue
                if nbr in seen: # cycle detected
                    return True
                else:
                    seen.add(nbr)
                    dfs(nbr, node)
            return False

        cycle = dfs(0, 0)
        return False if (cycle or len(seen) != n-1) else True

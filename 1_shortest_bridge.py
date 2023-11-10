# Link: https://leetcode.com/problems/shortest-bridge/submissions/

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < n and not vis[r][c] and grid[r][c] == 1):
                return
            vis[r][c] = True
            edges.append((r, c))
            for dr, dc in dirs:
                r2, c2 = r + dr, c + dc
                dfs(r2, c2)

        
        def bfs():
            flips = 0
            
            q = deque()
            for edge in edges:
                q.append(edge)
            while q:
                for pt_no in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        r2, c2 = r + dr, c + dc
                        if 0 <= r2 < n and 0 <= c2 <n:
                            if grid[r2][c2] == 1 and not vis[r2][c2]:
                                return flips
                            if not vis[r2][c2]:
                                q.append((r2, c2))
                                vis[r2][c2] = True
                flips += 1
            return -1
                                
        
        n = len(grid)
        edges = []
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        vis = [[False for _ in range(n)] for _ in range(n)]
        
        first = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1 and not first:
                    dfs(r, c)
                    first = True
                    break
            if first:
                break
            
        flips = bfs()
        return flips

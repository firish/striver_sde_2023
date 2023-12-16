# connected components in a matrix

# Link: https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def is_valid(r, c, m, n):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True
        
        def mark(r, c, m, n, vis, grid):
            dirs= [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for pt in dirs:
                dx = r + pt[0]
                dy = c + pt[1]
                if is_valid(dx, dy, m, n):
                    if grid[dx][dy] == "1" and not vis[dx][dy]:
                        vis[dx][dy] = True
                        mark(dx, dy, m, n, vis, grid)
            return 1
        
        res = 0
        vis = [[False for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not vis[r][c]:
                    vis[r][c] = True
                    res += mark(r, c, m, n, vis, grid)
        return res

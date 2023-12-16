# Graph
# BFS, from multiple start points at same time

# Link: https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        # check if the cordinates exist within the grid
        def is_valid(r, c):
            if 0 <= r < m and 0<= c < n: return True
            return False
        
        # find all rotten oranges at t = 0
        rotten = []
        total_fresh = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    total_fresh += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))
        
        q = deque()
        q.append(rotten)
        time = 0
        while q:
            curr_rotten = q.popleft()
            next_rotten = []
            
            for curr_orange in curr_rotten:
                curr_orange_r, curr_orange_c = curr_orange
                vis[curr_orange_r][curr_orange_c] = True
                
                for direction in directions:
                    delta_r, delta_c = direction
                    next_orange_r = curr_orange_r + delta_r
                    next_orange_c = curr_orange_c + delta_c
                    if is_valid(next_orange_r, next_orange_c):
                        if not vis[next_orange_r][next_orange_c]:
                            if grid[next_orange_r][next_orange_c] == 1: # fresh
                                next_rotten.append((next_orange_r, next_orange_c))
                                vis[next_orange_r][next_orange_c] = True
                                total_fresh -= 1
                            
            if len(next_rotten) > 0:
                q.append(next_rotten)
                time += 1
        
        return time if total_fresh == 0 else -1

# DFS
# Boundary checking and logic

# Link: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        def is_valid(r, c):
            if 0 <= r < m and 0 <= c < n:
                return True
            return False
        
        def is_boundary(r, c):
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                return True
            return False
        
        def dfs(r, c):
            vis[r][c] = True
            for d in dirs:
                row, col = r + d[0], c + d[1]
                if is_valid(row, col):
                    if board[row][col] == "O":
                        if not vis[row][col]:
                            dfs(row, col)
            
        
        vis = [[False for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if is_boundary(row, col):
                    if not vis[row][col]:
                        if board[row][col] == "O":
                            dfs(row, col)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    if not vis[row][col]:
                        board[row][col] = "X"
        return board

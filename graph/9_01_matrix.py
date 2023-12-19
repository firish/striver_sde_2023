# A good problem
# You have to apply BFS for list of points at every step

# Link: https://leetcode.com/problems/01-matrix/discuss/4423474/Python-BFS-(easy-to-read-code)

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        # 4-adjacent directions
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        zeros = []
        # get all zeros
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    zeros.append((row, col))
                    vis[row][col] = True
        
        # check if the cell being visited is valid
        def is_valid(r, c):
            if 0 <= r < m and 0 <= c < n:
                return True
            return False
        
        # Do a BFS from multiple nodes (all zeros at current distance) 
        # at the same time
        dist = 0
        q = deque()
        q.append(zeros)
        while q:
            dist += 1
            cordinates = q.popleft()
            next_cordinates = []
            for cordinate in cordinates:
                r, c = cordinate
                for d in directions:
                    row = r + d[0]
                    col = c + d[1]
                    if is_valid(row, col):
                        if not vis[row][col]:
                            vis[row][col] = True
                            res[row][col] = dist
                            next_cordinates.append((row, col))
            if len(next_cordinates) > 0:
                q.append(next_cordinates)
        return res
        

# BFS of a matrix
# conditionally connected components

# Link: https://leetcode.com/problems/flood-fill/

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append([sr, sc])
        vis = {(sr, sc): 1}
        pixel = image[sr][sc]
        nbrs = [[-1,0], [0,1], [1,0], [0,-1]]
        
        while len(q) > 0:
            point = q.popleft()
            r, c = point[0], point[1]
            image[r][c] = color
            for i in range(4):
                r2, c2 = r+nbrs[i][0], c+nbrs[i][1]
                if not (r2 < 0 or c2 < 0 or r2 >= len(image) or c2 >= len(image[0])):
                    if image[r2][c2] == pixel:
                        if (r2, c2) not in vis:
                            q.append([r2, c2])
                            vis[(r2, c2)] = 1
        return image

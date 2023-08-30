# Find link at: https://practice.geeksforgeeks.org/problems/shortest-source-to-destination-path3544/1

from collections import deque

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0] == 0: return -1
        
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        vis = [[False for _ in range(M)] for _ in range(N)]
        q = deque()
        q.append([0, 0, 0])
        dist = 0
        while q:
            r, c, dist = q.popleft()
            if r == X and c == Y: return dist
            vis[r][c] = True
            for i in range(4):
                r2 = r + dirs[i][0]
                c2 = c + dirs[i][1]
                if r2 >= 0 and r2 < N and c2 >= 0 and c2 < M and A[r2][c2] == 1 and not vis[r2][c2]:
                    vis[r2][c2] = True
                    q.append([r2, c2, dist+1])
        return -1

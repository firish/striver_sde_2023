# Link: https://leetcode.com/problems/number-of-enclaves/discuss/4498828/Python-simple-BFS-solution
# Fine ones that can not exit 4-direcrionally

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        seen=set()
        directions=((1,0),(0,1),(0,-1),(-1,0))
        def solve(x,y):
            nonlocal seen
            seen.add((x,y))
            q=collections.deque()
            q.append((x,y))
            ans=0
            flag=True
            while q:
                i,j=q.popleft()
                if i==0 or j==0 or i==m-1 or j==n-1:
                    flag=False
                for d in directions:
                    new_i,new_j=i+d[0],j+d[1]
                    if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j]==1 and (new_i,new_j) not in seen:
                        q.append((new_i,new_j))
                        seen.add((new_i,new_j))
                ans+=1
            return ans if flag else 0
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen: 
                    res+=solve(i,j)
        return res

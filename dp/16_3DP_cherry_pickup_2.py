# Ques Link: https://leetcode.com/problems/cherry-pickup-ii/
# Tut link: https://www.youtube.com/watch?v=QGfn7JeXK54&list=PLg0aancPZwRazLXPEW-vu517p3gXVCn0b&index=13

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # NOTE: r1 will always be equal to r2 (r)
        def cherry_pickup(r, c1, c2, dp):
            # safety, out of bound case
            if r < 0 or r >= m or c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return -10**10

            # base case
            if r == m-1:
                if c1 != c2:
                    return grid[r][c1] + grid[r][c2]
                else: 
                    return grid[r][c1]
            
            # memo check
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]

            maxi = 0
            if c1 != c2:
                cherries = grid[r][c1] + grid[r][c2]
            else: 
                cherries = grid[r][c1]
            
            # we want to check [1, -1], [1, 0], [1, 1] for each robot
            # so total 9 combinations (for robo 1's [1, -1] we go to robos 2's [1, -1], [1, 0], [1, 1] and so on)
            for c1_ in [-1, 0, 1]:
                for c2_ in [-1, 0, 1]:
                    maxi = max(maxi, cherries + cherry_pickup(r+1, c1+c1_, c2+c2_, dp))
            dp[r][c1][c2] = maxi
            return dp[r][c1][c2]
    
        # get the dp array
        # 3D DP -> (r, c1, c2)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        return cherry_pickup(0, 0, n-1, dp)

                

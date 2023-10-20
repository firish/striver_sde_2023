# Link: https://leetcode.com/problems/cherry-pickup/

# solution
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1: return 0
        
        def is_valid(r, c):
            if 0 <= r < n and 0 <= c < n and grid[r][c]  != -1:
                return True
            return False
        
        # Intuition
        # track robo 1 and robo 2 together
        # [IMP] track robo 2 in reverse (we want to have a 3D dp and not 4D)
        
        # Now since we can go right as well, we need to find a way
        # to get r1 from r2 or vice-versa
        # after t steps, the positions of both persons are:
        # r1 + c1 = t
        # r2 + c2 = t
        # If both robots start at the origin, r + c of their current cell
        # tells the number of moves they have made
        # using this two equations,
        # r1 + c1 = r2 + c2
        # hence, r2 = r1 + c1 - c2
        # now we can use a 3D DP, instead of 4D
        
        def pickup(r, c1, c2):
            # base case
            if r == n-1 and c1 == n-1 and r+c1-c2 == n-1 and c2 == n-1:
                # don't return twice as only 1 robo can pick up the cherry
                return grid[r][c1] 
            
            # memo check
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            
            # max cherries at current index
            # make sure you pick cherries only once if robots are at same index
            if c1 == c2 and r == (r+c1-c2):
                cherries = grid[r][c1]
            else:
                cherries = grid[r][c1] + grid[r+c1-c2][c2]
                
            
            s1, s2, s3, s4 = -10**12, -10**12, -10**12, -10**12
            # when robo1 goes down
            if is_valid(r+1, c1):
                # robo 2 can go down
                if is_valid((r+c1-c2)+1, c2):
                    s1 = cherries + pickup(r+1, c1, c2)
                # robo 2 can go right
                if is_valid((r+c1-c2), c2+1):
                    s2 = cherries + pickup(r+1, c1, c2+1)
            
            # when robo1 goes right
            if is_valid(r, c1+1):
                # robo 2 can go down
                if is_valid((r+c1-c2)+1, c2):
                    s3 = cherries + pickup(r, c1+1, c2)
                # robo 2 can go right
                if is_valid((r+c1-c2), c2+1):
                    s4 = cherries + pickup(r, c1+1, c2+1)
            
            # memoize
            dp[r][c1][c2] = max(s1, s2, s3, s4)
            return dp[r][c1][c2]
        
        # create DP state 
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        
        cherries = pickup(0, 0, 0)
        return 0 if cherries < 0 else cherries

# Link: https://leetcode.com/submissions/detail/1227235050/

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if not grid:
            return False
        
        m, n = len(grid), len(grid[0])
        moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        
        total = (m*n) # number of squares
        mapping = {}
        
        # get the (row, col) of the travel sequence given
        for row in range(m):
            for col in range(n):
                mapping[grid[row][col]] = (row, col)
        
        # a valid combination only starts at top-left
        if mapping[0] != (0, 0):
            return False 
        
        # traverse the path, from 0 to total
        # if any consequitive numbers are not a valid knight move, return False
        for square in range(0, total-1):
            curr = mapping[square]
            nxt = mapping[square + 1]
            legal_move = False
            for move in moves:
                if curr[0] + move[0] == nxt[0] and curr[1] + move[1] == nxt[1]:
                    legal_move = True
                    break

            if not legal_move:
                return False
        
        return True
            
            

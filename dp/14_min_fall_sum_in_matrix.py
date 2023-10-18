# Link: https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1: return matrix[0][0]
        
        def is_valid(r, c, n):
            if 0 <= r < n and 0 <= c < n: return True
            return False
        
        def fall(row, col, n, matrix, dp):
            if row == n-1:
                return matrix[row][col]
            
            if dp[row][col] != 10**12:
                return dp[row][col]
            
            left, down, right = 10**12, 10**12, 10**12
            if is_valid(row+1, col-1, n):
                left = matrix[row][col] + fall(row+1, col-1, n, matrix, dp)
            if is_valid(row+1, col, n):
                down = matrix[row][col] + fall(row+1, col, n, matrix, dp)
            if is_valid(row+1, col+1, n):
                right = matrix[row][col] + fall(row+1, col+1, n, matrix, dp)
            
            dp[row][col] = min(left, down, right)
            return dp[row][col]
        
        n = len(matrix)
        dp = [[10**12 for _ in range(n)] for _ in range(n)]
        for col in range(n):
            fall(0, col, n, matrix, dp)
        return min(dp[0])

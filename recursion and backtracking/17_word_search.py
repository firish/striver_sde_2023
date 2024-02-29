# Link: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        m = len(board)
        n = len(board[0])
        
        if len(word) > m*n:
            return False
        if m == 1 and n == 1:
            return board[0][0] == word
        
        def isValid(row, col, vis):
            if row < 0 or col < 0 or row >= m or col >= n or (row, col) in vis:
                return False
            return True
        
        def check(ind, curr, i, j, vis):
            if ind >= len(word) or ind >= m*n:
                return False
            if ind == len(word)-1:
                return ''.join(curr) == word

            if word[ind] != board[i][j]:
                return False
            else:
                for d in dirs:
                    r = i + d[0]
                    c = j + d[1]
                    if isValid(r, c, vis):
                        vis.add((r, c))
                        chk = check(ind + 1, curr + [board[r][c]], r, c, vis)
                        if chk:
                            return True
                        vis.remove((r, c))
        
        for r in range(0, m):
            for c in range(0, n):
                vis = set()
                if board[r][c] == word[0]:
                    vis.add((r, c))
                    chk = check(0, [board[r][c]], r, c, vis)
                    if chk: 
                        return True
        return False

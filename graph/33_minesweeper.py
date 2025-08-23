# LC 529 (Medium)
# Mine Sweeper
# URL: https://leetcode.com/problems/minesweeper/

# My Soln:
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        def is_valid(r, c):
            return True if 0 <= r < m and 0 <= c < n else False
        
        def is_mine(r, c):
            return board[r][c] == 'M'
        
        def reveal_mine(r, c):
            board[r][c] = 'X'
        
        def is_empty(r, c):
            return board[r][c] == 'E'
        
        def is_blank(r, c):
            return board[r][c] == 'B'
        
        def set_empty_score(r, c):
            score = 0
            for d in dirs:
                rd, cd = d
                r2, c2 = r + rd, c + cd
                if is_valid(r2, c2) and is_mine(r2, c2):
                    score += 1
            board[r][c] = str(score)
        
        def change_empty_to_blank(r, c):
            if board[r][c] == "0":
                board[r][c] = 'B'
        
        seen = set()
        def click_board(r, c):
            seen.add((r, c))

            if is_mine(r, c):
                reveal_mine(r, c)
            
            if is_empty(r, c):
                set_empty_score(r, c)
                change_empty_to_blank(r, c)

            if is_blank(r, c):
                for d in dirs:
                    rd, cd = d
                    r2, c2 = r + rd, c + cd
                    if is_valid(r2, c2) and (r2, c2) not in seen:
                        seen.add((r2, c2))
                        click_board(r2, c2)
        
        click_board(click[0], click[1])
        return board


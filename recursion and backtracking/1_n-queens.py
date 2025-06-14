# The famous N-queens problem
# Every row and col should have exactly 1 queen
# No queens should attack each other

# This solution is better than standard solutions
# As we are not looping again and again to check if queens are being attacked
# we only do 4 look-up operations that each take O(1) time.

from collections import defaultdict 

N = 4
board = [["_" for _ in range(N)] for _ in range(N)]

rows = defaultdict(bool)
cols = defaultdict(bool)
pos_diag = defaultdict(bool)
neg_diag = defaultdict(bool)

def checker(row, col):
    global rows, cols, pos_diag, neg_diag
    #  check if queen is being attacked from any direction
    if rows[row] or cols[col] or pos_diag[row+col] or neg_diag[row-col]: return False
    return True

def n_queens(n, col, board):
    global rows, cols, pos_diag, neg_diag

    # break condition
    if col >= n:
        for row in board: print(row)
        print('\n')
        return
    
    # Try to place a queen at all rows in the current column
    for row in range(0, n, 1):
        if checker(row, col):
            # setup
            board[row][col] = 'Q'
            rows[row] = True
            cols[col] = True
            pos_diag[row+col] = True
            neg_diag[row-col] = True

            # recursive call
            n_queens(n, col+1, board)

            # Backtracking
            board[row][col] = '_'
            rows[row] = False
            cols[col] = False
            pos_diag[row+col] = False
            neg_diag[row-col] = False

n_queens(N, 0, board)   





### second pass
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # game board
        board = [['.']*n for _ in range(n)]
        queens = 0

        # game state trackers
        invalid_rows = set()
        invalid_cols = set()
        invalid_pos_diags = set() # r - c for all pts on pos diag is same
        invalid_neg_diags = set() # r + c for all pts on neg diag is same

        def check_position_validity(r, c):
            # queen attack horizontal
            if r in invalid_rows:
                return False
            # queen attack vertical
            if c in invalid_cols:
                return False
            # queen attack diagonal
            if r + c in invalid_neg_diags:
                return False
            if r - c in invalid_pos_diags:
                return False
            return True

        res = []
        def get_all_board_positions(c):
            nonlocal board, queens, invalid_rows, invalid_cols, invalid_pos_diags, invalid_neg_diags

            # end condition - successfully placed the queens
            if c >= n-1 and queens == n:
                res.append([''.join(r) for r in board])
                return
            
            for r in range(0, n):
                if check_position_validity(r, c):
                    # place queen
                    invalid_rows.add(r)
                    invalid_cols.add(c)
                    invalid_neg_diags.add(r+c)
                    invalid_pos_diags.add(r-c)
                    board[r][c] = 'Q'
                    queens += 1
                    # recurse
                    get_all_board_positions(c+1)
                    # backtrack
                    invalid_rows.remove(r)
                    invalid_cols.remove(c)
                    invalid_neg_diags.remove(r+c)
                    invalid_pos_diags.remove(r-c)
                    board[r][c] = '.'
                    queens -= 1
                
        
        # start placement from 1st col
        get_all_board_positions(0)

        return res

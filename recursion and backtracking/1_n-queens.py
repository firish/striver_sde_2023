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
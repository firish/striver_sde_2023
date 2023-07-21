class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_valid(board, row, col, number):
            box = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2}
            start = {(0,0):(0,0), (0,1):(0,3), (0,2):(0,6), (1,0):(3,0), (1,1):(3,3), (1,2):(3,6), (2,0):(6,0), (2,1):(6,3), (2,2):(6,6)}
            offset = {0:(0,0), 1:(0,1), 2:(0,2), 3:(1,0), 4:(1,1), 5:(1,2), 6:(2,0), 7:(2,1), 8:(2,2)}
            
            # First, find which 3x3 box do the row and column belong to 
            box_r, box_c = box[row], box[col]
            # Find the starting row and column index of box of the box
            pos = start[(box_r, box_c)]
            
            for ind in range(0, 9, 1):
                # row condition check
                if board[row][ind] == number: return False
                # col condition check
                if board[ind][col] == number: return False
                
                # 3x3 box condition check
                # calculate offset positions
                off = offset[ind]
                r = pos[0] + off[0]
                c = pos[1] + off[1]
                if board[r][c] == number: return False
            
            return True
            
        
        for row in range(0, 9, 1):
            for col in range(0, 9, 1):
                # check for blank spots to fill
                if board[row][col] == ".":
                    # try and fill all posible values (1 to 9)
                    for num in range(1, 10, 1):
                        # check if placing this number is a legal move
                        if is_valid(board, row, col, str(num)):
                            board[row][col] = str(num)
                            if(self.solveSudoku(board)):
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True

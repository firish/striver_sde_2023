class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        grid = [['.' for _ in range(3)] for _ in range(3)]
        scores = [[0 for _ in range(3)] for _ in range(3)]
        xc, oc = 0, 0
        for r in range(3):
            for c in range(3):
                if board[r][c] != " ":
                    grid[r][c] = board[r][c]
                    if grid[r][c] == 'X':
                        scores[r][c] = 1
                        xc += 1
                    else:
                        scores[r][c] = -1
                        oc += 1    
        
        # check game-win condition
        game_win = False
        wins = []
        winner = ''
        wins.append(scores[0][0] + scores[0][1] + scores[0][2])
        wins.append(scores[1][0] + scores[1][1] + scores[1][2])
        wins.append(scores[2][0] + scores[2][1] + scores[2][2])
        wins.append(scores[0][0] + scores[1][0] + scores[2][0])
        wins.append(scores[0][1] + scores[1][1] + scores[2][1])
        wins.append(scores[0][2] + scores[1][2] + scores[2][2])
        wins.append(scores[0][0] + scores[1][1] + scores[2][2])
        wins.append(scores[0][2] + scores[1][1] + scores[2][0])

        f1, f2 = False, False
        for win in wins:
            if win == 3:
                game_win = True
                winner = 'X'
                f1 = True
                
            if win == -3:
                game_win = True
                winner = 'O'
                f2 = True
        
        # if both players win, its wrong
        if f1 and f2:
            return False
        # if x won, o cnt should be less than x
        if winner == 'X':
            if oc >= xc:
                return False
        # if o won, x and o cnt should be same
        if winner == 'O':
            if xc != oc:
                return False
        
        # if here, it means the pattern on board is a draw
        # check if the current pattern could be formed taking turns
        def validate(chance, vis):
            for r in range(3):
                for c in range(3):
                    if grid[r][c] == ".": continue

                    if chance == "1":
                        if grid[r][c] == "X" and not vis[r][c] and chance == "1":
                            vis[r][c] = True
                            x = validate("2", vis)
                            if not x:
                                return False
                        else:
                            continue
                    else:
                        if grid[r][c] == "O" and not vis[r][c] and chance == "2":
                            vis[r][c] = True
                            o = validate("1", vis)
                            if not o:
                                return False
                        else:
                            continue
            return False
        
        vis = [[False for _ in range(3)] for _ in range(3)]
        validate("1", vis)
        for r in range(3):
            for c in range(3):
                if grid[r][c] != ".":
                    if not vis[r][c]:
                        return False
        return True

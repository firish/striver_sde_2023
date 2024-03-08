# Great question

# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/

from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def is_valid(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            return True
        
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def is_ocean(r, c):
            if r < 0 or c < 0:
                return 0 # pacific
            elif r >= m or c >= n:
                return 1 # atlantic
            else:
                return 2 # not an ocean cell
            
        res = []
        for r in range(m):
            for c in range(n):
                seen = set()
                q = deque()
                q.append((r, c))
                pacific, atlantic = False, False
                while q:
                    curr_r, curr_c = q.popleft()
                    for d in dirs:
                        nxt_r = curr_r + d[0]
                        nxt_c = curr_c + d[1]
                    
                        status = is_ocean(nxt_r, nxt_c)
                        if status == 0:
                            pacific = True
                        elif status == 1:
                            atlantic = True
                        else:
                            if is_valid(nxt_r, nxt_c):
                                    curr_height = heights[curr_r][curr_c]
                                    nxt_height = heights[nxt_r][nxt_c]
                                    if curr_height >= nxt_height:
                                        if (nxt_r, nxt_c) not in seen:
                                            q.append((nxt_r, nxt_c))
                                            seen.add((nxt_r, nxt_c))
                                            
                if pacific and atlantic:
                    res.append([r, c])
                
        return res

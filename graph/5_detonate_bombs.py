# create graph
# BFS for each node

# Link: https://leetcode.com/problems/detonate-the-maximum-bombs/


class Solution:
    def dist(self, x, y):
        return sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:        
        res = 1
        for i in range(len(bombs)):
            current_res = 1
            visited = set()
            visited.add(i)
            q = collections.deque([i])
            while q:
                node = q.popleft()
                for c in range(len(bombs)):
                    if c not in visited and self.dist(bombs[node], bombs[c]) <= bombs[node][2]:
                        q.append(c)
                        visited.add(c)
                        current_res += 1
                        
            res = max(res, current_res)
                
        return res


from collections import deque

class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        adj_list = [[] for _ in range(n)]

        # Precompute which bombs can trigger each other
        for i in range(n):
            for j in range(n):
                if i != j:
                    dist = (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2
                    if dist <= bombs[i][2]**2:
                        adj_list[i].append(j)
        # print(adj_list)
        
        def bfs(start):
            seen = set()
            q = deque([start])
            while q:
                node = q.popleft()
                for nei in adj_list[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            return len(seen) + 1 # for original bomb

        return max(bfs(i) for i in range(n))

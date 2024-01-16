# Link: https://leetcode.com/problems/course-schedule-ii/submissions/


# sol
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0: return []
        
        stack = []
        vis = [False for _ in range(numCourses)]
        path_vis = [False for _ in range(numCourses)]
        
        graph = defaultdict(list)
        for edge in prerequisites:
            ai, bi = edge[0], edge[1]
            graph[bi].append(ai)
        
        def dfs(node):
            vis[node] = True
            path_vis[node] = True
            
            for nbr in graph[node]:
                if not vis[nbr]:
                    if not dfs(nbr):
                        return False
                else:
                    if path_vis[nbr]:
                        return False
            
            path_vis[node] = False
            stack.append(node)
            return True
        
        for node in range(0, numCourses):
            if not vis[node]:
                if not dfs(node):
                    return []
        return stack[::-1]
                    
                    

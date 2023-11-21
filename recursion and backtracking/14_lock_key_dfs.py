# Link: https://leetcode.com/problems/keys-and-rooms/submissions/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(key, vis):
            vis.add(key)
            for nbr in rooms[key]:
                if nbr not in vis:
                    dfs(nbr, vis)
                
        vis = set()
        vis.add(0)
        dfs(0, vis)

        return len(vis) == len(rooms)

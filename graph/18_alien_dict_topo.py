# famous ques
# alien dict
# GFG prob/LinkedIn prem

# Link: https://www.geeksforgeeks.org/problems/alien-dictionary/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=alien-dictionary

# Sol
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        def check(s1, s2):
            l = min(len(s1), len(s2))
            res = []
            for i in range(l):
                if s1[i] != s2[i]:
                    res = [ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')]
                    break
            return res
        
        indegrees = [0]*K
        g = defaultdict(list)
        for i in range(len(alien_dict)-1):
            s1, s2 = alien_dict[i], alien_dict[i+1]
            res = check(s1, s2)
            if res != []:
                g[res[1]].append(res[0])
                indegrees[res[0]] += 1

        q = deque()
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(node)
        
        topo = []
        while len(q) > 0:
            node = q.popleft()
            for nbr in g[node]:
                indegrees[nbr] -= 1
                if indegrees[nbr] == 0:
                    q.append(nbr)
            topo.append(chr(ord('a') + node))

        return topo[::-1]

# Great problem
# Coding Ninja / Linkedin Prem problem
# uses Kahns Algo and the concept of indegrees

# Link:

# Sol
from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    indegrees = [0]*(n+1)
    for ai, bi in prerequisites:
        graph[bi].append(ai)
        indegrees[ai] += 1
    
    q = deque()
    non_zero_indegree = False
    for node, indegree in enumerate(indegrees):
        # we skip 0, as node counting starts from 1
        if node == 0: continue
        if indegree == 0:
            non_zero_indegree = True
            q.append((node, 1)) # (course, semester)
    # if indegree of all nodes is non-zero
    # topo sort / linear conditional ordering is not possible
    if not non_zero_indegree:
        return -1
    
    max_semester = 1
    topo = []
    while len(q) > 0:
        node, semester = q.popleft()
        max_semester = max(max_semester, semester)
        for nbr in graph[node]:
            indegrees[nbr] -= 1
            if indegrees[nbr] == 0:
                q.append((nbr, semester+1))
        topo.append(node)

    if len(topo) < n:
        return -1
    # remember, if you have to submit course ordering, reverse topo
    return max_semester

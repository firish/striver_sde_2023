# Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        
        res = [[root.val]]
        q = deque()
        for child in root.children:
            q.append(child)
        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(level)
        return res

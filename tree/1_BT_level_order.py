# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        q = deque()
        if root: q.append(root)

        while q:
            level = len(q)
            level_nodes = []
            for _ in range(level):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level_nodes.append(node.val)
            res.append(level_nodes)
            
        return res
        
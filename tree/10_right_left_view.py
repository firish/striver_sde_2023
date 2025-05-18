# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        q = deque()
        if root: q.append((root))

        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(node.val)
        
        return res

    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        q = deque()
        if root: q.append((root))

        while q:
            l = len(q)
            first = True
            for _ in range(l):
                node = q.popleft()
                if first:
                  res.append(node.val)
                  first = False
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
        
        return res

# OPTION 2 for left side view
# instead of this,
        if node.left: 
            q.append(node.left)
        if node.right: 
            q.append(node.right)
# do the reverse, right first and then left, 
# and then add the last node itself.



# 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        # write level order traversal
        q = deque()
        q.append([root])
        res = [root.val]
        while len(q) > 0:
            curr = q.popleft()
            level = []
            for node in curr:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if len(level) > 0:
                q.append(level)
                res.append(level[-1].val)
                # replace with res.append(level[0].val) for left view
        return res

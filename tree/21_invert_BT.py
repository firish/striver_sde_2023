# LC 226 - ez
# URL: https://leetcode.com/problems/invert-binary-tree/

# BOTTOM UP (TAIL RECURSION)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        if root.right or root.left:
            root.left, root.right = root.right, root.left

        return root

# TOP UP (HEAD RECURSION)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # swap children
        root.left, root.right = root.right, root.left
        # iterate over all nodes in order
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        return root


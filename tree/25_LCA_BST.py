# LC: 235 (Medium)
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Exploit bst
        # its a sorted tree, so both values may be at left or right
        # but if values are split, then the current node is the LCA
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left          # both targets lie left
            elif p.val > root.val and q.val > root.val:
                root = root.right         # both targets lie right
            else:                          # split point is LCA
                return root

# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(troot):
            if not troot:
                return None
            if troot.val == p.val or troot.val == q.val:
                return troot
            
            left = lca(troot.left)
            right = lca(troot.right)
            
            if not left and not right:
                return None
            elif not left and right:
                return right
            elif left and not right:
                return left
            else:
                return troot
        
        return lca(root)

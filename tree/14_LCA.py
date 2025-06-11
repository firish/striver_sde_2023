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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case, return if root in null
        if not root:
            return None

        # Traverse the tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If you found one of the nodes, return its value upwards
        if root.val == p.val or root.val == q.val:
            return root
        
        # if both vals are none, return none
        # if one val is none, return the other one
        # if both vals are not none, return root.val (lca)
        # print(root.val, left, right)
        if left and right:
            return root
        elif not right and left:
            return left
        elif not left and right:
            return right
        else:
            return None

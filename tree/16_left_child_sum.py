# Link: https://leetcode.com/problems/sum-of-left-leaves/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        def fll(node, d):
            if not node:
                return
            # print(node.val, d)
            
            if node.left:
                fll(node.left, 'l')
            
            if node.right:
                fll(node.right, 'r')
            
            if not node.left and not node.right:
                if d == 'l':
                    res[0] += node.val
            return
        
        fll(root, 'r')
        return res[0]

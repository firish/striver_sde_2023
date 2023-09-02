# Link: https://leetcode.com/problems/diameter-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Note, in python, variables are directly passed by reference. 
        # However, if you run into scope issues, try using an one element array instead of a variable.
        maxi = [0]
        def get_height(node, maxi):
            if not node: return 0
            
            lh = get_height(node.left, maxi)
            rh = get_height(node.right, maxi)
            if lh + rh > maxi[0]: maxi[0] = lh + rh
            
            return max(lh, rh) + 1
        
       
        h= get_height(root, maxi)
        return maxi[0]

 

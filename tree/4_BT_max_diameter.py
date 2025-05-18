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


# 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def get_height(node, max_diameter):
            if not node:
                return 0
            
            # travese
            left_height = get_height(node.left, max_diameter)
            right_height = get_height(node.right, max_diameter)

            # calculate diameter
            max_diameter[0] = max(max_diameter[0], left_height + right_height)

            # calculate height
            return max(left_height, right_height) + 1
        
        max_diameter = [0]
        max_height = get_height(root, max_diameter)
        return max_diameter[0]


 

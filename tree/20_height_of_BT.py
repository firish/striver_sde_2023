# link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_height(node):
            if not node: 
                return 0
            
            # traverse
            left = get_height(node.left)
            right = get_height(node.right)

            return max(left, right) + 1
        
        return get_height(root)

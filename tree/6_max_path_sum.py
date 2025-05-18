# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/

class Solution:
    def __init__(self):
        self.maxi = float('-inf')
        
    def get_sum(self, root):
        if not root:
            return 0
        
        # Get the maximum sum from the left and right subtrees
        ls = max(self.get_sum(root.left), 0)
        rs = max(self.get_sum(root.right), 0)
        
        # Update the global maximum with the maximum path sum that includes the current node
        self.maxi = max(self.maxi, ls + rs + root.val)
      
        return max(ls, rs) + root.val
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.get_sum(root)
        return self.maxi


# 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def get_path_sum(node, max_path_sum):
            if not node:
                return 0
            
            # travese
            left_sum = max(get_path_sum(node.left, max_path_sum), 0)
            right_sum = max(get_path_sum(node.right, max_path_sum), 0)

            # calculate diameter
            current_path_sum = left_sum + right_sum + node.val
            max_path_sum[0] = max(max_path_sum[0], current_path_sum)

            # calculate sum
            return max(left_sum, right_sum) + node.val
        
        max_path_sum = [-10**10]
        _ = get_path_sum(root, max_path_sum)
        return max_path_sum[0]

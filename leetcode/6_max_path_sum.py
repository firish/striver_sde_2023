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

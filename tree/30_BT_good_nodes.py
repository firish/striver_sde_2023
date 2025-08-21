# LC 1448 (Medium)
# Number of good nodes
# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxi):
            # break cond
            if not node:
                return 0
            
            # track good nodes
            curr = 0
            if node.val >= maxi:
                maxi = node.val
                curr = 1
            
            left = dfs(node.left, maxi)
            right = dfs(node.right, maxi)

            # return
            return left + right + curr
        
        return dfs(root, root.val)

# LC 938 - Easy
# URL: https://leetcode.com/problems/range-sum-of-bst/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def get_values_in_range(root):
            nonlocal res
            if not root:
                return
            if low <= root.val <= high:
                res += root.val
            if root.left and (root.left.val >= low or root.left.val <= high):
                get_values_in_range(root.left)
            if root.right and (root.right.val >= low or root.right.val <= high):
                get_values_in_range(root.right)

# OPTIMIZED
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal total
            if not node:
                return

            # Value inside range ➜ add and explore both sides
            if low <= node.val <= high:
                total += node.val
                dfs(node.left)
                dfs(node.right)

            # Current value too large ➜ only left side can help
            elif node.val > high:
                dfs(node.left)

            # Current value too small ➜ only right side can help
            else:  # node.val < low
                dfs(node.right)

        dfs(root)
        return total

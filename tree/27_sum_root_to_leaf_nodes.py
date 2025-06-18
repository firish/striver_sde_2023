# LC 129
# Medium

# URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []
        def traverse(root, curr):
            # stop case
            if not root:
                return
            
            # update path sum
            curr += str(root.val)

            # traverse
            traverse(root.left, curr)
            traverse(root.right, curr)

            # add to list if path sum is completed
            if not root.left and not root.right:
                res.append(curr)
        
        traverse(root, '')

        sum = 0
        for path_sum in res:
            sum += int(path_sum)
        return sum

# LC 108 (easy)
# URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def make_tree(nums):
            if len(nums) <= 0:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            left = make_tree(nums[:mid])
            right = make_tree(nums[mid+1:])
            node.left = left
            node.right = right
            return node
        
        bst = make_tree(nums)
        return bst

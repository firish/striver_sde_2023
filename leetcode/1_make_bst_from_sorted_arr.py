# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def make_bst(lower, upper):
            # base condition, here, child node
            if lower == upper:
                return None
            
            
            mid = (lower + upper) // 2
            node = TreeNode(nums[mid])
            node.left = make_bst(lower, mid)
            node.right = make_bst(mid+1, upper)
            return node
        
        root = make_bst(0, len(nums))
        return root
        

# LC easy
# Link: https://leetcode.com/problems/same-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            else:
                if not check(t1.left, t2.left):
                    return False
                if not check(t1.right, t2.right):
                    return False
                return True
            
        return check(p, q)

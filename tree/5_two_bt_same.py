# Link: https://leetcode.com/problems/same-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q: return False
        if not q and p: return False
        if not p and not q: return True
        
        if p.val != q.val:
            return False
        is_left_same = self.isSameTree(p.left, q.left)
        is_right_same = self.isSameTree(p.right, q.right)
        if not is_left_same or not is_right_same:
            return False
        else:
            return True

# Another code, self
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q:
            return True
        if p and not q or q and not p:
            return False
        
        if p.val != q.val:
            return False
        left =  self.isSameTree(p.left, q.left)
        if not left:
            return False
        right = self.isSameTree(p.right, q.right)
        if not right:
            return False
        
        return True


# better sol: https://www.youtube.com/watch?v=BhuvF_-PWS0&list=PLJ_vPQ_vraNz90tiB1HNgUWjivW07RcXC&index=16

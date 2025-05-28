# Link: https://leetcode.com/problems/balanced-binary-tree/submissions/

# Ques summary
# Height balanced BT: height(left subtree) -  height(riight subtree) <= 1 for all nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root: return 0

            left_height = check(root.left)
            if left_height == -1: return -1
            right_height = check(root.right)
            if right_height == -1: return -1
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1 
        
        res = check(root)
        if res == -1: return False
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def find_height(root):
            if not root:
                return 0

            left = find_height(root.left)
            if left == -1:
                return -1
            right = find_height(root.right)
            if right == -1:
                return -1
                
            if abs(left-right) > 1:
                return -1

            return max(left, right) + 1
        
        return find_height(root) != -1

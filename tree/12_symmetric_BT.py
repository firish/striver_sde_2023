# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def sym(left_root, right_root):
            if left_root == None or right_root == None:
                return left_root == right_root
            else:
                if left_root.val != right_root.val:
                    return False
                else:
                    x = sym(left_root.left, right_root.right)
                    y = sym(left_root.right, right_root.left)
                    if x and y:
                        return True
                    return False
         
        if root.left == None or root.right == None:
                return root.left == root.right
        else:
            return sym(root.left, root.right)
        

# Same code, written at a different time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(left, right):
            if not left or not right:
                return left == right
            
            if left.val != right.val:
                return False
            left_right = check(left.left, right.right)
            if not left_right:
                return False
            right_left = check(left.right, right.left)
            if not right_left:
                return False
            
            return True
        
        return check(root, root)

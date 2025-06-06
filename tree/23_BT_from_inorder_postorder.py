# LC 106 - medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # Inorder -> left, root, right
        # Inorder -> first is always leftmode node of tree
        # Postorder -> left, right, node
        # Postorder -> Last node is always root

        # For such questions, always,
        # 1. try to get root
        # 2. find index of roor
        # 3. split inorder by index of root to get left and right subtree
        # 4. recurse

        def build_tree(inorder, postorder):
            
            if len(inorder) <= 0 or len(postorder) <= 0: # leaf node reached
                return None
            root = TreeNode(postorder[-1])
            index = inorder.index(root.val)
            # everything to right of index is right subtree
            root.right = build_tree(inorder[index+1:], postorder[index:-1])
            # everything to left of index is left subtree
            root.left = build_tree(inorder[:index], postorder[:index])
            return root
        
        return build_tree(inorder, postorder)

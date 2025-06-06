# LC 105 - medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Inorder -> left, root, right
        # Inorder -> first is always leftmode node of tree
        # Preorder -> root, left, right
        # Preorder -> first node is always root

        # For such questions, always,
        # 1. try to get root
        # 2. find index of root
        # 3. split inorder by index of root to get left and right subtree
        # 4. recurse

        def build_tree(inorder, preorder):
            
            if len(inorder) <= 0 or len(preorder) <= 0: # leaf node reached
                return None
            root = TreeNode(preorder[0])
            index = inorder.index(root.val)
            # everything to left of index is left subtree
            root.left = build_tree(inorder[:index], preorder[1:index+1])
            # everything to right of index is right subtree
            root.right = build_tree(inorder[index+1:], preorder[index+1:])
            return root
        
        return build_tree(inorder, preorder)

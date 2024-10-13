# LC Medium
# Blind 75
# Question Number 105

# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/

# NC: https://www.youtube.com/watch?v=ihj4IQGZ2zc

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Trick
        # Preorder ALWAYS has the node first. 
        # But you don't know the size of either branch.
        # Inorder ALWAYS has the left branch to the left of the node, and right branch right of the node.
        # So now you know the size of each branch.

        # base case
        # returns None for leaf nodes
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        # Since preorder has the first node
        root = TreeNode(preorder[0])

        # Now find the size of left and right subtree
        root_index = inorder.index(root.val)

        # Now for getting the left subtree
        root.left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])

        # Now getting the right subtree
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        # return the construced tree
        return root

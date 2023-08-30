# Find problem link at: https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1

# Problem name: Right View of a BT

# Intuition: To find the right view of a binary tree, you can perform a level order traversal of the tree and print the last node at each level.
# This can be accomplished using a queue data structure.

# Code:
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root is None:
            return []
        
        queue = []
        res = []
        queue.append(root)
        
        while queue:
            levelNodes = len(queue)
            for i in range(levelNodes):
                node = queue.pop(0)
                # if it's the last node of this level, add it to the result
                if i == levelNodes - 1:
                    res.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

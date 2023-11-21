# Creating a Binary Tree

class Node:
    # Initialize the Tree Node
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self, node):
        if not node: return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)
    
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
    
    def postorder(self, node):
        if not node: return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
        






# Python3 program for boundary traversal of binary tree

# Actual solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # Null case
        if not root:
            return []
        
        # helper to check if a node is a leaf 
        def is_leaf(node):
            if not node.left and not node.right:
                return True
            return False

        # Head Reccursion - left boundary
        def get_left(node, left):
            if node.left and not is_leaf(node.left):
                left.append(node.left.val)
                get_left(node.left, left)
            if not node.left and node.right and not is_leaf(node.right):
                left.append(node.right.val)
                get_left(node.right, left)
        
        # Tail Reccursion - right boundary - in reverse order
        def get_right(node, right):
            if node.right and not is_leaf(node.right):
                get_right(node.right, right)
                right.append(node.right.val)
                
            if not node.right and node.left and not is_leaf(node.left):
                get_right(node.left, right)
                right.append(node.left.val)
                
        # Head recursion - bottom boundary - left to right traversal
        def get_bottom(node, bottom):
            if is_leaf(node):
                bottom.append(node.val)
                return
            
            if node.left:
                get_bottom(node.left, bottom)
            if node.right:
                get_bottom(node.right, bottom)

        left = []
        if root.left:
            if not is_leaf(root.left):
                left = [root.left.val]
                get_left(root.left, left)
        # print(left)

        right = []
        if root.right:
            if not is_leaf(root.right):
                get_right(root.right, right)
                right.append(root.right.val)
        # print(right)

        bottom = []
        if root and not is_leaf(root):
            get_bottom(root, bottom)
        # print(bottom)

        return [root.val] + left + bottom + right



# LOL
class Node:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

# A simple function to print leaf nodes (Bottom) of a Binary Tree
def printLeaves(root):
	if(root):
		printLeaves(root.left)
		
		# Print it if it is a leaf node
		if root.left is None and root.right is None:
			print(root.data)
      
		printLeaves(root.right)

# A function to print all left boundary nodes, except the leaf nodes. 
# Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
	
	if(root):
		if (root.left):
			
			# to ensure top down order, print the node
			# before calling itself for left subtree
			print(root.data)
			printBoundaryLeft(root.left)
		
		elif(root.right):
			print (root.data)
			printBoundaryLeft(root.right)

  else:
      pass
		  # do nothing if it is a leaf node, this way we
		  # avoid duplicates in output


# A function to print all right boundary nodes, except the leaf nodes. 
# Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
	
	if(root):
		if (root.right):
			# to ensure bottom up order, first call for
			# right subtree, then print this node
      # tail recursion
			printBoundaryRight(root.right)
			print(root.data)
		
		elif(root.left):
			printBoundaryRight(root.left)
			print(root.data)
  else:
      pass
		  # do nothing if it is a leaf node, this way we 
		  # avoid duplicates in output


# A function to do boundary traversal of a given binary tree
def printBoundary(root):
	if (root):
		print(root.data)
		
		# Print the left boundary in top-down manner
		printBoundaryLeft(root.left)

		# Print all leaf nodes
		printLeaves(root.left)
		printLeaves(root.right)

		# Print the right boundary in bottom-up manner
		printBoundaryRight(root.right)


# Driver program to test above function
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
printBoundary(root)


Find link at: https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

#Function to find the lowest common ancestor in a BST. 
def LCA(root, n1, n2):
    #code here.
    while root:
        # If both n1 and n2 are smaller than root, then LCA lies in left
        if root.data > n1 and root.data > n2:
            root = root.left

        # If both n1 and n2 are greater than root, then LCA lies in right
        elif root.data < n1 and root.data < n2:
            root = root.right
        # If neither of the above conditions is true, 
        # it means n1 is in one subtree and n2 is in another subtree, 
        # so this node is the lowest common ancestor.
        else:
            break

    return root

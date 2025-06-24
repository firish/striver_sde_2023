# LC Ez
# Morris Traversal is med-to-hard

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Morris Traversal
        # Time O(2N) -> O(N)
        # Space O(1), no reccursion stack

        # Idea - Threaded Binary Tree
        # at every node (current), check for node.left
        # Case 1, if node.left exists
        #   traverse to rightest node of the left subtree

        #   Case 1.1
        #   if rightmost node points to null, connect its next to the current node
        #   this is called a thread
        #   move left

        #   Case 1.2
        #   if rightmost node points to curr, you have encountered a pre-existing thread, clean it to avoid looping the same path
        #   this means you have covered this subtree, add curr (root) to inorder
        #   left subtree and root is done, move right 
        
        # Case 2
        #   If no left node exists, you are at the root
        #   add curr (root) to inorder
        #   traverse right

        # implementation
        inorder = []
        curr = root
        while curr:
            # check for left node
            # case 1, left subtree found
            if curr.left:
                leaf = curr.left
                while leaf.right and leaf.right != curr: # check for curr as well to avoid any cycles because of threads
                    leaf = leaf.right
                # if the right is null, set the thread
                if leaf.right == None:
                    leaf.right = curr
                    # move left to the next node
                    curr = curr.left
                # if the right is curr, move back and remove the thread
                if leaf.right == curr:
                    leaf.right = None
                    # add the root and move right as the left and root is done
                    inorder.append(curr.val)
                    curr = curr.right

            # case 2, no left subtree
            else:
                # add the root and move right
                inorder.append(curr.val)
                curr = curr.right
        
        return inorder





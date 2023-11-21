# Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/


# code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        def make_bst(root, lower, upper):
            # safety case
            if not root:
                return None
            
            # base case
            if lower == upper:
                return None
            
            # Binary search
            mid = (lower + upper) // 2
            node = TreeNode(arr[mid])
            node.left = make_bst(node, lower, mid)
            node.right = make_bst(node, mid+1, upper)
            return node
            
        
        # get length of linked list and convert to arr
        pos = head
        arr = []
        l = 0
        while pos:
            l += 1
            arr.append(pos.val)
            pos = pos.next
            
        root = make_bst(head, 0, l)
        return root

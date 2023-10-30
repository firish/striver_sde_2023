# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Link: https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        store = []
        p = head
        while p:
            store.append(p)
            p = p.next
        
        i, j = 0, len(store)-1
        while i < j:
            store[i].next = store[j]
            store[j].next = store[i+1]
            i += 1
            j -= 1
        store[i].next = None
        
        return head
            
        
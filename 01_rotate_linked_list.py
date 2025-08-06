# LC 61 (Medium)
# URL: https://leetcode.com/problems/rotate-list/

# My soln
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases
        if not head or k == 0:
            return head

        # Get the length of the linked list and leave a pointer at the tail
        p = head
        cnt = 0
        while p:
            cnt += 1
            tail = p
            p = p.next
        
        # Get the index of the break point
        # the break point should be the new head
        # everything from break to tail will be appended to the left of current head
        if cnt == k or cnt == 1:
            return head
        if cnt > k:
            ind = cnt - k
        else:
            ind = cnt - (k % cnt)
        
        # traverse to break point
        p = head
        for _ in range(ind-1):
            p = p.next
        
        # Step 1: Attach tail to left of current head
        tail.next = head 
        # step 2: make break point the new head
        head = p.next
        # step 3: make the node before the break the tail
        p.next = None

        return head

        
        

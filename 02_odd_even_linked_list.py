# LC 328 (Medium)
# URL: https://leetcode.com/problems/odd-even-linked-list/description/

# My soln
# 1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if not head or not head.next:
            return head

        # odd and even list heads
        odd_head = head
        even_head = head.next

        # we need the tail of odd list
        # as this will become the head of the even list
        odd_tail = None
        
        # two pointers for stiching odd and even lists
        p = odd_head
        q = even_head
        while p and q:
            # stich even indices
            if q: # if not at end of list
                p.next = q.next
                # if p.next is None, we are at end of odd list
                if not p.next:
                    odd_tail = p
                p = p.next

            # stich odd indices
            if p: # if not at end of list
                q.next = p.next
                 # if p.next is None, we are at end of odd list
                if not p.next:
                    odd_tail = p
                q = q.next

        # Attach even list to end of odd list
        odd_tail.next = even_head

        return odd_head


# Optimized, and easier to read
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle corner cases
        if head == None or head.next == None: return head
        
        # Use two pointers, odd and even
        # In each iteration, link next odd element to current odd element (1->3)
        # and next even element to current even element (2->4)
        # this creates two links, one of odd nodes and one of even nodes
        # after traversing the entire linked list,
        # connect last node of odd links with first node of even links
        odd, even = head, head.next
        temp = even # hold the start of even nodes
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = temp # c

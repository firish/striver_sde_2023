# LC 2674 (Medium) (Premium)
# URL: https://leetcode.com/problems/split-a-circular-linked-list/

# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        # get length of the 2 circular linked lists
        cnt = 0
        p = head
        while True:
            cnt += 1
            if p.next == head:
                tail = p
                break
            else:
                p = p.next
        n1, n2 = math.ceil(cnt/2), math.floor(cnt/2)
        
        # create the first circular linked list
        ch1 = head
        for _ in range(1, n1):
            ch1 = ch1.next
        # after traversing till end of LL1, get LL2 head
        ch2 = ch1.next
        # make LL1 circular
        ch1.next = head
        
        # create the second circular linked list
        tail.next = ch2

        return [head, ch2]

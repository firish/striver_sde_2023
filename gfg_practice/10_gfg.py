Link at: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        current = head
        next = None
        previous = None
        count = 0

        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = previous
            previous = current
            current = next
            count += 1

        # next is now a pointer to (k+1)th node
        if next is not None:
            head.next = self.reverse(next, k)

        # previous is new head
        return previous

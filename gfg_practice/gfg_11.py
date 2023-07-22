Find ques link at: https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        nums = set()
        curr = head
        prev = None
        while curr:
            if curr.data in nums:
                while curr and curr.data in nums:
                    curr = curr.next
                prev.next = curr
                if curr:
                    nums.add(curr.data)
            else:
                nums.add(curr.data)
            prev = curr
            if curr:
                curr = curr.next
        return head

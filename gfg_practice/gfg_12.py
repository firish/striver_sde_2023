Question Link at: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        z, o, t = 0, 0, 0
        p = head
        while p:
            if p.data == 0: z += 1
            elif p.data == 1: o += 1
            else: t += 1
            p = p.next
        
        p = head
        while p:
            if z > 0:
                p.data = 0
                z -= 1
            elif o > 0:
                p.data = 1
                o -= 1
            else:
                p.data = 2
                t -= 1
            p = p.next
        return head

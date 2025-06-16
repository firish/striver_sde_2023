# LC Medium (prem)
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root_to_p = set()
        root_to_p.add(p)
        curr = p
        while curr:
            root_to_p.add(curr)
            curr = curr.parent

        curr = q
        while curr:
            if curr in root_to_p:
                return curr
            curr = curr.parent

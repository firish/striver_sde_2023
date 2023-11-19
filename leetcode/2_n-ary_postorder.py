# Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def post(node, res):
            if not node: 
                return []
        
            for child in node.children:
                post(child, res)
            res += [node.val]
            
        res = []
        post(root, res)
        return res

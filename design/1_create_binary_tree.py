# Links: https://leetcode.com/problems/create-binary-tree-from-descriptions/submissions/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        parents = defaultdict(int)
        for vals in descriptions:
            parent_val, child_val, is_left = vals[0], vals[1], vals[2]
            
            if parent_val not in nodes:
                parent_node = TreeNode(parent_val)
                nodes[parent_val] = parent_node
            else:
                parent_node = nodes[parent_val]
            
            if child_val not in nodes:
                child_node = TreeNode(child_val)
                nodes[child_val] = child_node
            else:
                child_node = nodes[child_val]
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            parents[parent_val] += 0 
            parents[child_val] += 1
        
        for node_value, num_parent in parents.items():
            if num_parent == 0:
                return nodes[node_value]
        return None
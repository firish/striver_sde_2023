# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque()
        q.append(root)
        
        flag = True
        while q:
            l = len(q)
            nodes = []
            for _ in range(l):
                node = q.popleft()
                nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                res.append([node for node in nodes])
                flag = False
            else:
                res.append([node for node in nodes[::-1]])
                flag = True
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Null case
        if not root:
            return []

        # Initialize queue with root    
        q = deque()
        q.append([root])
        res = [[root.val]]

        # toggle for zig-zag
        left_to_right = True 

        while len(q) != 0:
            # toggle the zig-zag flag
            left_to_right = not left_to_right

            # store nodes on that level
            level = []
            nodes = q.popleft()
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            # if nodes exist on that level, add according to the zig-zag flag
            if len(level) > 0:
                q.append(level) # continue traversal 
                if left_to_right:
                    res.append([node.val for node in level])
                else:
                    res.append([node.val for node in level[::-1]]) # add in reverse
        
        return res
            
            
                
            
            

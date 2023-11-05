# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        mapping = defaultdict(lambda: defaultdict(list))
        q = deque()
        # (root, vertical (x-cord), level (y-cord))
        if root: q.append((root, 0, 0))

        while q:
            l = len(q)
            for _ in range(l):
                node, vertical, level = q.popleft()
                mapping[vertical][level].append(node.val)
                
                if node.left: 
                    q.append((node.left, vertical-1, level+1))
                if node.right: 
                    q.append((node.right, vertical+1, level+1))
        
        
        for vertical, levels in sorted(mapping.items()):
            curr_vertical = []
            for level, nodes in sorted(levels.items()):
                curr_vertical += sorted(nodes)
            res.append(curr_vertical)
        return res

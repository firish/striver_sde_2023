# Link: https://leetcode.com/problems/binary-tree-paths/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def paths(troot, path):
            if not troot: return False
            
            path.append(str(troot.val))
            left = paths(troot.left, path)
            right = paths(troot.right, path)
            
            if not left and not right:
                res.append("->".join(path))
            
            path.pop()
            return True
        
        
        if not root: return []
        paths(root, [])
        return res

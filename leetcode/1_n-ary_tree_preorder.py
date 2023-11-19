# Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def pre(node, res):
            if not node: 
                return []
        
            res += [node.val]
            for child in node.children:
                pre(child, res)
            
        res = []
        pre(root, res)
        return res

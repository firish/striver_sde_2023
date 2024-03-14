# LC Ez
# blind 75

# Link: https://leetcode.com/problems/subtree-of-another-tree/submissions/

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return same_tree(q.left, p.left) and same_tree(q.right, p.right)
        
        def helper(node, subroot):
            if not node:
                return False
            if node.val == subroot.val:
                if same_tree(node, subroot):
                    return True
            return helper(node.left, subroot) or helper(node.right, subroot)
        
        return helper(root, subRoot)
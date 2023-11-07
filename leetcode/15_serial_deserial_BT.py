# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('#')
        return ','.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        q = deque()
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q.append(root)
        
        i = 1
        while q:
            curr = q.popleft()
            # left child
            if data[i] != '#':
                node = TreeNode(int(data[i]))
                curr.left = node
                q.append(node)
            else:
                curr.left = None
            i += 1
            
            # right child
            if data[i] != '#':
                node = TreeNode(int(data[i]))
                curr.right = node
                q.append(node)
            else:
                curr.right = None
            i += 1
            
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

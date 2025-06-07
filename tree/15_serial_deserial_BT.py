# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

# BFS
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
        
        
# DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.serial = []
        self.root = None
        self.ind = 0
        self.deserial = []

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.serial.append("#")
        else:
            self.serial.append(str(root.val))
            self.serial.append("(")
            self.serialize(root.left)
            self.serial.append(")")
            self.serial.append("(")
            self.serialize(root.right)
            self.serial.append(")")
        return ''.join(self.serial)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # end case
        if self.ind >= len(data):
            return self.root
        
        # leaf node
        if self.ind < len(data) and data[self.ind] == '#':
            self.ind += 1 # '#'
            return None
        
        # Parse integer (handle multi-digit numbers)
        start = self.ind
        while self.ind < len(data) and (data[self.ind] == '-' or data[self.ind].isdigit()):
            self.ind += 1
        val = int(''.join(data[start:self.ind]))
        node = TreeNode(val)

        # build left subtree
        if self.ind < len(data) and data[self.ind] == '(':
            self.ind += 1 # '('
            node.left = self.deserialize(data)
            if self.ind < len(data) and data[self.ind] == ')':
                self.ind += 1 # '('
        
        # build right subtree
        if self.ind < len(data) and data[self.ind] == '(':
            self.ind += 1 # '('
            node.right = self.deserialize(data)
            if self.ind < len(data) and data[self.ind] == ')':
                self.ind += 1 # '('

        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

# codec = Codec()
# print(codec.serialize(root))

# data = codec.serial
# root = codec.deserialize(data)
# print(root)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))




### GENERAL ALGO
# 1. Be Explicit About Nulls
# Always mark None or null nodes explicitly (e.g., with '#' or 'null') so the structure can be faithfully reconstructed.

# 2. Decide Between Preorder and BFS
# Preorder DFS (Root-Left-Right) is ideal for recursive solutions and is easy to serialize with parentheses or delimiters.

# Level-order (BFS) is good when you want constant time for deserialization per node, often used with queue and ','-delimited formats (like LeetCode's [1,2,3,null,null,4,5]).

# 3. Make Your Format Human-Readable
# Use characters like (, ), or , to mark structure. Avoid ambiguous formats like "123##" unless the structure is fixed and well understood.

# 4. Avoid Class-Level State
# Instead of using self.serial, prefer passing a list or string as a local variable and returning the result. This avoids shared state bugs when using multiple instances (like ser, deser in LeetCode).

# 5. Always Reset Index in Deserialization
# Set self.ind = 0 at the start of deserialize() — crucial when using recursive parsing.

class Codec:

    def serialize(self, root):
        def dfs(node):
            if not node:
                return '#'
            return f"{node.val}({dfs(node.left)})({dfs(node.right)})"
        
        return dfs(root)

    def deserialize(self, data):
        self.ind = 0  # reset index for each deserialization

        def dfs():
            if data[self.ind] == '#':
                self.ind += 1
                return None

            # Parse number (multi-digit and negative)
            start = self.ind
            if data[self.ind] == '-':
                self.ind += 1
            while self.ind < len(data) and data[self.ind].isdigit():
                self.ind += 1
            node = TreeNode(int(data[start:self.ind]))

            # Parse left
            if self.ind < len(data) and data[self.ind] == '(':
                self.ind += 1
                node.left = dfs()
                self.ind += 1  # skip ')'

            # Parse right
            if self.ind < len(data) and data[self.ind] == '(':
                self.ind += 1
                node.right = dfs()
                self.ind += 1  # skip ')'

            return node

        return dfs()



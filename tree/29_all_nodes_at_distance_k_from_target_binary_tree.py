# LC 863
# Medium
# URL: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # intuition
        # 1st bfs; build parent
        # second bfs; only for k times, but travel left, right, parent

        # easy edge case
        if k == 0:
            return [target.val]

        # build the parent map
        parents = defaultdict(TreeNode) # int key -> treenode val
        parents[root.val] = None
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                parents[curr.left.val] = curr
            if curr.right:
                q.append(curr.right)
                parents[curr.right.val] = curr

        # bfs upto k steps
        q = deque()
        q.append([target])
        vis = set()
        vis.add(target.val)
        dist = 0
        while dist != k and q:
            dist += 1
            curr_hop_nodes = q.popleft()
            next_hop_nodes = []
            for node in curr_hop_nodes:
                if node.left and node.left.val not in vis:
                    next_hop_nodes.append(node.left)
                    vis.add(node.left.val)
                if node.right and node.right.val not in vis:
                    next_hop_nodes.append(node.right)
                    vis.add(node.right.val)
                node_parent = parents[node.val]
                if node_parent and node_parent.val not in vis:
                    next_hop_nodes.append(node_parent)
                    vis.add(node_parent.val)

            if dist == k:
                return [node.val for node in next_hop_nodes]
            else:
                q.append(next_hop_nodes)
        

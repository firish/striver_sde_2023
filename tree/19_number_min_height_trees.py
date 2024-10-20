# LC Medium
# tough question
# Centroid Tree Algorithm

# URL: https://leetcode.com/problems/minimum-height-trees/discuss/5939437/Python-Centroid-Algorithm-with-explanation-beats-100

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
    # Efficient Solution with O(n) Time Complexity
    # ALGO: finding the centroids of the tree. 
    # A tree can ONLY have one or two centroids
    # and these centroids are the roots of the Minimum Height Trees (MHTs).

    # Algorithm Overview
    # Identify Leaves: Initialize all nodes with degree 1 (leaves).
    # Remove the leaves from the tree.
    # After removing, update the degrees of the neighboring nodes.
    # If any neighbor's degree becomes 1, it becomes a leaf for the next iteration.
    # Repeat Until only 1 or 2 Nodes Remain:
    # The last remaining nodes are the centroids of the tree.
    
    # Explanation
    # Why This Works:
    # Removing leaves layer by layer is similar to peeling the tree from the outside towards the center.
    # The nodes that remain at the end are the ones that minimize the maximum distance to all other nodes, i.e., they minimize the tree's height.
    
        # Solution
        # Edge case: single node
        if n == 1:
            return [0]
        
        # Build the graph
        graph = defaultdict(list)
        degree = [0] * n  # Degree of each node
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        remaining_nodes = n
        while remaining_nodes > 2:
            # trim the leaves
            leaves_size = len(leaves)
            remaining_nodes -= leaves_size
            
            # adjust neighboring node's degree after trimming leaves
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)

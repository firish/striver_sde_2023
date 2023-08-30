# Find question link at: https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1

# Intuition:  we perform a DFS to build a dictionary with parent pointers and store it in the parent dictionary. 
# Then, we start from the given node and move upwards until we have moved 'k' steps or we have reached the root. 

def kthAncestor(root,k, node):
    #code here
    # traverse tree in dfs form to create the parent dict
    parent = {}
    def dfs(curr, prev):
        if curr is None:
            return
        parent[curr.data] = prev
        dfs(curr.left, curr)
        dfs(curr.right, curr)
    dfs(root, None)
    
    # traverse parent staring from node to check if ancestor exists
    if node in parent:
        while node in parent and k > 0:
            node = parent[node].data if parent[node] else None
            k -= 1
            
        if k == 0:
            return node if node else -1
            
    return -1

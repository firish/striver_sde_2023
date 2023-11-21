# A node of N-ary tree
class Node:
	def __init__(self, key):
		self.key = key
		self.children = []

# A utility function to create a new N-ary tree node
def newNode(key):
	temp = Node(key)
	return temp


def serialize(root, res):
	# Base case
	if not root:
		return

	res.append(str(root.key))
	res.append("(")
	for child in root.children:
		serialize(child, res)
	res.append(")")
	


def parse_node(s, index):
    if index >= len(s) or s[index] == ")":
        return (None, index)

    # Parse the root node
    node_val = ""
    while index < len(s) and s[index] not in "()":
        node_val += s[index]
        index += 1

    # The current character should be '('
    node = newNode(node_val)
    index += 1  # Skip past the '('

    # Parse children
    while s[index] != ")":
        child, index = parse_node(s, index)
        if child:
            node.children.append(child)
    
    # The current character should be ')'
    index += 1  # Skip past the ')'
    return (node, index)

# A utility function to create a dummy tree shown in above diagram
def createDummyTree():
	root = newNode('A')
	root.children = [newNode('B'), newNode('C'), newNode('D')]
	root.children[0].children = [newNode('E'), newNode('F')]
	root.children[2].children = [newNode('G'), newNode('H'), newNode('I'), newNode('J')]
	root.children[0].children[1].children = [newNode('K')]
	return root

def traverse(root):
    if root:
        print(root.key, end=" ")
        for child in root.children:
            traverse(child)

# Driver program to test above functions
def main():
	root = createDummyTree()
	print("Constructed N-Ary Tree from code is ")
	traverse(root)
	
	print('\n')
	res = []
	serialize(root, res)
	print(''.join(res))
	
	deserial_root, _ = parse_node(res, 0)
	print("Re-constructed N-Ary Tree from code is ")
	traverse(deserial_root)

if __name__ == '__main__':
	main()
print('')

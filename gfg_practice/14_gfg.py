Link at: https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1


if not root:
        return []

    # Create two stacks to store nodes of alternate levels
    s1 = []  # For levels to be printed from right to left
    s2 = []  # For levels to be printed from left to right

    # Push first level to first stack 's1'
    s1.append(root)

    result = []

    # Keep printing while any of the stacks has some nodes
    while s1 or s2:
        # Print nodes of current level from 's1' and push nodes of
        # next level to 's2'
        while s1:
            temp = s1.pop()
            result.append(temp.data)

            # Note that right child is pushed before left
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        # Print nodes of current level from 's2' and push nodes of
        # next level to 's1'
        while s2:
            temp = s2.pop()
            result.append(temp.data)

            # Note that left child is pushed before right
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)

    return result

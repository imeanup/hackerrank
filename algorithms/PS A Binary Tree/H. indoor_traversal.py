# Implement an inorder traversal without recursion


def inoder_traversal(tree):  # Time: O(n); space: O(h)
    s, result = [], []

    while s or tree:
        if tree:
            s.append(tree)
            # Going left.
            tree = tree.left

        else:
            # Going up.
            tree = s.pop()
            result.append(tree.data)
            # Going right.
            tree = tree.right

    return result


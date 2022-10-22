# Implement an inorder traversal with O(1) space.


def inorder_traversal(tree):  # Time: O(n) Space: O(1)
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from prev.
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                # Done with left, so go right if right is not empty. Otherwise,
                # go up.
                next = tree.right or tree.parent

        elif tree.left is prev:
            # We came up to tree from its left child.
            result.append(tree.data)
            # Done with left, so go right if right is not empty. Otherwise,
            # go up
            next = next.right or tree.parent
        # Done with both child, so move up.
        else:
            next = tree.parent

        prev, tree = tree, next
    return result

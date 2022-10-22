# Compute the exterior of a binary tree


def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right

    # Compute the nodes from the root of the leftmost
    # leaf followed by all the leaves in subtree.

    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (
            ([subtree] if is_boundary or is_leaf(subtree) else [])
            + left_boundary_and_leaves(subtree.left, is_boundary)
            + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)
        )

    # Compute the leaves in left-to-right order followed by the rightmost
    # leaf to the root path in subtree.
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (
            right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right)
            + right_boundary_and_leaves(subtree.right, is_boundary)
            + ([subtree] if is_boundary or is_leaf(subtree) else [])
        )

    return (
        [tree]
        + left_boundary_and_leaves(tree.left, is_boundary=True)
        + right_boundary_and_leaves(tree.right, is_boundary=True)
        if tree
        else []
    )


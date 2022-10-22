# Find a root to leaf path with specified sum


def has_path_sum(tree, remaining_weight):  # Time: O(n);Space: O(h)
    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data

    # Non-leaf.
    return has_path_sum(tree.left, remaining_weight - tree.data) or has_path_sum(
        tree.right, remaining_weight - tree.data
    )

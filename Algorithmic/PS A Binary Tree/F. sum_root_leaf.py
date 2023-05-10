# Sum the root to leaf path in a Binary Tree


def sum_root_to_leaf(tree, partial_path_sum=0):  # Space: O(h);Time: O(n)
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:  # Leaf.
        return partial_path_sum
    # Non-leaf.
    return sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(
        tree.right, partial_path_sum
    )


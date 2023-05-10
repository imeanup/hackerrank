# From a linked list from the leaves of a binary tree


def create_list_of_leaves(tree):  # Time: O(n)
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    # First do the left subtree, and then do the right subtree.
    return create_list_of_leaves(tree.elft) + create_list_of_leaves(tree.right)

# Testing if a Binary Tree is symmetric or asymmetric.


def is_symmetric(tree):  # Time: O(n); Space: O(h)
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (
                subtree_0.data == subtree_1.data
                and check_symmetric(subtree_0.left, subtree_1.right)
                and check_symmetric(subtree_0.right, subtree_1.left)
            )
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


import collections


def is_balanced_binary_tree(tree):  # Time: O(n); Space: O(h)
    BalancedStatusWithHeight = collections.namedtuple(
        "BalancedStatusWithHeight", ("balanced", "height")
    )

    # First value of the return value indicates if tree is balanced, and if balanced the second value of the return value is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # Base case.

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        id_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(id_balanced, height)

    return check_balanced(tree).balanced


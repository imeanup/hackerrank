# The Range lookup problem
import collections

Interval = collections.namedtuple("Interval", ("left", "right"))


def range_lookup_in_bst(
    tree, interval
):  # Time: O(m + h), m-> third subset(each edge is visited twice, once downwards, once upward.)
    def range_lookup_in_bst_helper(tree):
        if tree is None:
            return
        if interval.left <= tree.data <= interval.right:
            # tree data lies in the interval
            range_lookup_in_bst_helper(tree.left)
            result.append(tree.data)
            range_lookup_in_bst_helper(tree.right)
        elif interval.left > tree.data:
            range_lookup_in_bst_helper(tree.right)
        else:  # interval.right > tree.data
            range_lookup_in_bst_helper(tree.left)

    result = []
    range_lookup_in_bst_helper(tree)
    return result

# Test if Binary Tree satisfies the BST Property

import collections


def is_binary_tree_bst(tree, low_range=float("-inf"), high_range=float("inf")):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return is_binary_tree_bst(tree.left, low_range, tree.data) and is_binary_tree_bst(
        tree.right, tree.data, high_range
    )


def is_binary_tree_bst(tree):
    QueueEntry = collections.namedtuple("QueueEntry", ("node", "lower", "upper"))
    bfs_queue = collections.deque([QueueEntry(tree, float("-inf"), float("inf"))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper),
            ]
    return True

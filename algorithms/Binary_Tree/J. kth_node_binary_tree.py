#  Compute the K-th node in an inorder traversal


def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        # k-th node must be in right subtree of tree.
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right
        # k-th is iter itself
        elif left_size == k - 1:
            return tree
        # k-th node must be in left subtree of iter.
        else:
            tree = tree.left

        return None


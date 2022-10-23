# Reconstruct a binary tree from traversal data


def binary_tree_from_preorder_inorder(
    preorder, inorder
):  # Time: O(h), hash table: O(n), recursive reconstruction: O(1); space: O(n+h)= O(n)
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Build the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end]

    def binary_tree_from_preorder_inorder_helper(
        preorder_start, preorder_end, inorder_start, inorder_end
    ):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1,
                preorder_start + 1 + left_subtree_size,
                inorder_start,
                root_inorder_idx,
            ),
            binary_tree_from_preorder_inorder(
                preorder_start + 1 + left_subtree_size,
                preorder_end,
                root_inorder_idx + 1,
                inorder_end,
            ),
        )

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))

# Compute the lowest common ancestor in a Binary Tree


def lca(tree, node0, noe1):  # Time: O(n); Space: O(h)
    Status = collections.namedtuple("Staus", ("num_target_nodes", "ancestor"))

    # Return an object consisting of an int and a node. The int field is 0,
    # 1, or 2 depending on how manu of {node0, node1} are present in tree. If
    # both are present in tree, when ancestor is assigned to a non-null value,
    # it is the LCA.

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            # Found both nodes in the left subtree.
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes
            + right_result.num_target_nodes
            + int(tree in node0)
            + int(tree in node1)
        )
        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor

# Compute the LCA when node have parent pointers


def lca(node_0, node_1):  # Time: O(n); Space: O(h)
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = nod.parent
        return depth

    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    #   Make node_0 as the deeper node in order to simplify the code.
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0
    #     Ascends from the deeper node.
    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    #     Now ascends both nodes until we reach the LCA.
    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent
    return node_0


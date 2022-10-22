def tree_traversal(root):  # Time: O(n); Space: O(h); h-> height; min(h) = log n; max(h) = n
    if root:
        # Pre-order: Processes the root before the traversals of left and right childer.
        print("Preorder: %d" % root.data)
        tree_traversal(root.left)
        # In-order: Processes the root after the traversal of left child and before the traversal of right chiLd.
        print("Inorder: %d" % root.data)
        tree_traversal(root.right)
        # Post-order: Processes the root after the traversals of left and right chiLd.
        print("Postorder: %d" % root.data)

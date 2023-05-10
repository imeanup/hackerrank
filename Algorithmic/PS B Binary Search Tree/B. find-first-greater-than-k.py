# Find the first key greater than a given value in a BST


def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else: # Root and all keys in left subtree are <= k, so skip them.
            subtree = subtree.right

    return first_so_far

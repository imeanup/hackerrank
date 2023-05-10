# Build a minimum height BST from a sorted array


def build_min_height_bst_from_sorted_array(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return (
            BSTNode(A[mid]),
            build_min_height_bst_from_sorted_subarray(start, mid),
            build_min_height_bst_from_sorted_subarray(mid + 1, end),
        )

    return build_min_height_bst_from_sorted_subarray(0, len(A))

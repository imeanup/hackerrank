# Find the closest entries in three sorted arrays
import bintrees


def find_closest_elements_in_sorted_arrays(
    sorted_arrays,
):  # Time: O(n log k), where n is total number of elements in the k arrays.
    # special case n = 3, O(n log 3) = O(n)
    min_distance_so_far = float("inf")
    # Stores array iterators in each entry.
    iters = bintrees.RBTree()

    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)
    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        # Return if some array has no remaining elements.
        if next_min is None:
            return min_distance_so_far
        iters.insert((next_min, min_idx), it)

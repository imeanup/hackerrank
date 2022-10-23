# Test if three BST nodes are totally ordered


def pair_includes_ancestor_and_descendant_of_m(
    possible_anc_or_desc_0, possible_anc_or_desc_1, middle
):
    search_0, search_1 = possible_anc_or_desc_0, possible_anc_or_desc_1

    # Perform interleaved searching from possible_anc_or_desc_0 and
    # possible_anc_or_desc_1 for middle.
    while (
        search_0 is not possible_anc_or_desc_1
        and search_0 is not middle
        and (search_0 or search_1)
    ):
        if search_0:
            search_0 = search_0.left if search_0.data > middle.data else search_0.right
        if search_1:
            search_0 = search_1.left if search_1.data > middle.data else search_1.right

    # If both searches were unsuccessful, or we got from
    # possible_anc_pr_desc_0 to possible_anc_or_desc_1 without seeing middle,
    # or from posible_anc_or_desc_1 to possible_anc_or_desc_0 and
    # possible_anc_or_desc_1.

    if (
        (search_0 is not middle and search_1 is not middle)
        or search_0 is possible_anc_or_desc_1
        or search_1 is possible_anc_or_desc_0
    ):
        return False

    def search_target(source, target):
        while source and source is not target:
            source = source.left if source.data > target.data else source.right
        return source is target

    # If we get here, we already know one of possible-anc-or-desc-0 or
    # possible_anc_or_desc_1 has a path to middle. Check if middle has a path
    # to possible_anc_or_desc_1 or to possible_anc_or_desc_0.
    return search_target(
        middle, possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0
    )

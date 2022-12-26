"""
In-place comparision sort
Using Marcin Ciura's gap sequence, with an inner insertion sort.
Link: https://en.wikipedia.org/wiki/Shellsort
"""


def SHELLSORT(arr):
    n = len(arr)

    gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # Ciura gap sequence
    """
    Start with the largest gap and work down to a gap of 1
    similar to insertion sort but instead of 1, gap is being used in each step
    """
    for gap in gaps:
        i = gap
        """
        Do a gapped insertion sort for every elements in gaps
        Each loop leaves arr[0..gap-1] in gapped order
        """
        for i in range(n):
            """save arr[i] in temp and make a hole at position i"""
            temp = arr[i]
            j = i
            """shift earlier gap-sorted elements up until the correct location for arr[i] is found"""
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            """put temp (the original arr[i]) in its correct location"""
            arr[j] = temp
            i += gap


if __name__ == "__main__":
    import numpy

    array = numpy.random.randint(3000, size=(10))
    print(array)
    SHELLSORT(array)
    print(array)

# in-place Algorithms
##  Both insertion sort and selection sort are in-place algorithms, meaning they can each be implemented using at most a constant amount of additional space. The only operations performed on the array are comparisons and swaps between pairs of elements


# Not-in-place algorithms
## Merge sort uses a linear amount of temporary storage (temp) when combining the two halves, so it is `not in-place`.
#### While there exist algorithms that perform merging using no additional space, such implementations are substantially more complicated than the merge sort algorithm. Whether merge sort is stable depends on how an implementation breaks ties when merging. The above implementation is not stable, but it can be made stable with only a small modification

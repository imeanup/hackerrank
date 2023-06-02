// delete.cpp

#include "heap.h"

void deleteRoot(int arr[], int& n) {
    int lastElement = arr[n - 1];
    arr[0] = lastElement;
    n = n - 1;
    heapify(arr, n, 0);
}

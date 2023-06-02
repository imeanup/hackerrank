// main.cpp
#include "heap.h"

int main() {
    int arr[] = {10, 5, 3, 2, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    buildHeap(arr, n);

    cout << "Max-Heap: ";
    printArray(arr, n);

    insert(arr, n, 15);

    cout << "After inserting 15: ";
    printArray(arr, n);

    deleteRoot(arr, n);

    cout << "After deleting root: ";
    printArray(arr, n);

    return 0;
}


// MAX Heap 

/* 
g++ heapify.cpp delete.cpp build.cpp insert.cpp print.cpp main.cpp -o output
./output 
Max-Heap: 10 5 3 2 4 
After inserting 15: 15 5 10 2 4 3 
After deleting root: 10 5 3 2 4 
*/

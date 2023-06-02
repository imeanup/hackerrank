// insert.cpp
#include "heap.h"

void insert(int arr[], int& n, int key) {
    n++;
    int i = n - 1;
    arr[i] = key;
    while (i != 0 && arr[(i - 1) / 2] < arr[i]) {
        swap(arr[(i - 1) / 2], arr[i]);
        i = (i - 1) / 2;
    }
}
    

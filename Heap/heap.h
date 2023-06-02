// heap.h
#ifndef HEAP_H
#define HEAP_H

#include <iostream>
#include <algorithm>

using namespace std;

void heapify(int arr[], int n, int i);
void buildHeap(int arr[], int n);
void insert(int arr[], int& n, int key);
void deleteRoot(int arr[], int& n);
void printArray(int rr[], int n);

#endif

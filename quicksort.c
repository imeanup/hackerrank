#include <stdio.h>

void swap(int *x, int *y);
void quicksort(int array[], int length);
void quicksort_recursion(int arr[], int low, int high);
int partition(int array[], int low, int high);

int main(void)
{
    int a[] = {11, 12, 33, 44, 8, 15, 3, 9, 12, 45, 56, 45, 45};
    int len = 13;

    quicksort(a, len);

    for (int i = 0; i < len; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void swap(int *x, int *y)
{
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

void quicksort(int array[], int length)
{
    quicksort_recursion(array, 0, length - 1);
}

void quicksort_recursion(int arr[], int low, int high)
{
    if (low < high)
    {
        int pivot_index = partition(arr, low, high);
        quicksort_recursion(arr, low, pivot_index - 1);
        quicksort_recursion(arr, pivot_index + 1, high);
    }   
}

int partition(int array[], int low, int high)
{
    int pivot_value = array[high];
    int i = low;
    for (int j = low; j < high; j++)
    {
        if (array[j] <= pivot_value)
        {
            swap(&array[i], &array[j]);
            i++;
        }
    }
    swap(&array[i], &array[high]);
    return i;
}

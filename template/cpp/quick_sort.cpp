//  Quick Sort Template
#include <iostream>
#define INF (1 << 30)
#define MAXN 10
using namespace std;

void qsort(int * arr, int begin, int end){
    if (begin >= end - 1)
        return;
    int pivot = arr[begin];
    int p1 = begin, p2 = end - 1;
    while(p1 < p2){
        while (p1 < p2 && arr[p2] > pivot)
            p2--;
        if (p1 < p2)
            arr[p1++] = arr[p2];
        while (p1 < p2 && arr[p1] < pivot)
            p1++;
        if (p1 < p2)
            arr[p2--] = arr[p1];
    }
    arr[p1] = pivot;
    qsort(arr, begin, p1);
    qsort(arr, p1 + 1, end);
}

int main(){
    int arr[10] = {9, 1, 5, 3, 2, 8, 6, 4, 7, 0};
    qsort(arr, 0, 10);
    for (int i = 0; i < 10; i++)
        cout << arr[i] << endl;
    return 0;
}
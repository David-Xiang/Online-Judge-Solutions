// LeetCode 945
// Minimum Increment to Make Array Unique
class Solution {
    public int minIncrementForUnique(int[] A) {
        qsort(A, 0, A.length);
        int sum = 0;
        for (int i = 1; i < A.length; i++){
            if (A[i] > A[i-1])
                continue;
            sum += A[i-1]+1-A[i];
            A[i] = A[i-1]+1; 
        }
        return sum;
    }
    void qsort(int[] arr, int begin, int end){
        if (begin + 1 >= end)
            return;
        int pivot = arr[begin];
        int v1 = begin, v2 = end - 1;
        while(v1 < v2){
            while(v1 < v2 && arr[v2] > pivot)
                v2--;
            if (v1 < v2)
                arr[v1++] = arr[v2];
            while(v1 < v2 && arr[v1] < pivot)
                v1++;
            if (v1 < v2)
                arr[v2--] = arr[v1];
        }
        arr[v1] = pivot;
        qsort(arr, begin, v1);
        qsort(arr, v1+1, end);
    }
};

public class LC945{
    public static void main(String[] args){
        int [] arr = {3,2,1,2,1,7};
        Solution solution = new Solution();
        System.out.println(solution.minIncrementForUnique(arr));
    }
};
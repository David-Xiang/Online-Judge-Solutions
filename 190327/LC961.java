// LeetCode 961
// N-Repeated Element in Size 2N Array
// Search
// Solution1: qsort O(NlogN)
// Solution2: repeat elements' distance <= 3 O(N)
// Solution3: bucket (or hash) O(N)

class Solution {
    public int repeatedNTimes(int[] A) {
        qsort(A, 0, A.length);
        int n = A.length/2;
        if (A[n-1] == A[n-2])
            return A[n-1];
        else
            return A[n];
    }
    void qsort(int[] arr, int begin, int end){
        if (begin + 1 >= end)
            return;
        int pivot = arr[begin];
        int v1 = begin, v2 = end-1;
        while (v1 < v2){
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
}
public class LC961{
    public static void main(String [] args){
        int [] arr = {5,1,5,2,5,3,5,4};
        Solution solution = new Solution();
        System.out.println(solution.repeatedNTimes(arr));
    }
}
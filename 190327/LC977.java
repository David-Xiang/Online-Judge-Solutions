// LeetCode 977
// Squares of a Sorted Array
// Two Pointer

class Solution {
    public int[] sortedSquares(int[] A) {
        int len = A.length;
        int v1 = 0, v2 = len - 1;
        int count = len-1;
        int [] res = new int [len];

        while(v1 < v2){
            int tmp = abs(A[v1]) > abs(A[v2]) ? abs(A[v1++]) : abs(A[v2--]);
            res[count--] = tmp * tmp;
        }
        res[count--] = abs(A[v1]) * abs(A[v1]);
        return res;
    }
    int abs(int a){
        return a > 0 ? a : -a;
    }
}

public class LC977{
    public static void main(String [] args){
        int [] arr = {-7,-3,2,3,11};
        Solution solution = new Solution();
        int [] res = solution.sortedSquares(arr);
        for (int i : res){
            System.out.println(i);
        }
    }
}
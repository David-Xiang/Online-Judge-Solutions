/**
 * LeetCodeOffer 04 Easy
 * Search a 2D Matrix
 * Array
 */

public class LCOF04 {
    public static void main(String [] args){
        int [][] arr = new int[][] {
                {1, 4, 7, 11, 15},
                {2, 5, 8, 12, 19},
                {3, 6, 9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}
        };
        Solution solution = new Solution();
        System.out.println(solution.findNumberIn2DArray(arr, 5)); // return true
        System.out.println(solution.findNumberIn2DArray(arr, 20)); // return false
    }

    static
    class Solution {
        public boolean findNumberIn2DArray(int[][] matrix, int target) {
            if (matrix.length == 0 || matrix[0].length == 0) {
                return false;
            }
            int r = matrix.length, c = matrix[0].length;
            int i = r - 1, j = 0;
            while (i < r && i >= 0 && j < c && j >= 0) {
                if (matrix[i][j] == target) {
                    return true;
                } else if (matrix[i][j] < target) {
                    j++;
                } else {
                    i--;
                }
            }
            return false;
        }
    }
}
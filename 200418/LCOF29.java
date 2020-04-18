/**
 * LeetCodeOffer 29 Easy
 * Spiral Matrix
 * Array
 */

public class LCOF29 {
    public static void main(String [] args){
        int [][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        Solution solution = new Solution();
        int [] arr = solution.spiralOrder(matrix);
        for (int i: arr) {
            System.out.println(i);
        }
    }

    static
    class Solution {
        public int[] spiralOrder(int[][] matrix) {
            if (matrix.length == 0 || matrix[0].length == 0) {
                return new int[0];
            }
            int row = matrix.length, col = matrix[0].length;
            int [] res = new int [row*col];
            int count = 0;
            int l = 0, r = col, u = 0, d = row;
            for (int dir = 0; l < r && u < d; dir++) { // dir 0 向右 1 向下 2 向左 3 向上
                switch (dir % 4) {
                    case 0:
                        for (int i = l; i < r; i++) {
                            res[count++] = matrix[u][i];
                        }
                        u++;
                        break;
                    case 1:
                        for (int i = u; i < d; i++) {
                            res[count++] = matrix[i][r-1];
                        }
                        r--;
                        break;
                    case 2:
                        for (int i = r - 1; i >= l; i--) {
                            res[count++] = matrix[d-1][i];
                        }
                        d--;
                        break;
                    case 3:
                        for (int i = d - 1; i >= u; i--) {
                            res[count++] = matrix[i][l];
                        }
                        l++;
                        break;
                }
            }
            return res;
        }
    }
}
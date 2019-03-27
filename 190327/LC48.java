// LeetCode 48
// Rotate Image
// IN PLACE rotate the image

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n/2; i++)
            rotateLayer(matrix, i, i, n-2*i);
    }
    public void rotateLayer(int[][] matrix, int x, int y, int len){
        // (x, y) is up-left point of the layer
        for (int i = 0; i < len - 1; i++){
            int tmp = matrix[x][y+i];
            matrix[x][y+i] = matrix[x+len-i-1][y];
            matrix[x+len-i-1][y] = matrix[x+len-1][y+len-1-i];
            matrix[x+len-1][y+len-1-i] = matrix[x+i][y+len-1];
            matrix[x+i][y+len-1] = tmp;
        }
    }
}

public class LC48{
    public static void main(String [] args){
        int [][] m1 = new int[][]{
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        Solution solution = new Solution();
        solution.rotate(m1);
        for (int [] i: m1){
            for (int j: i)
                System.out.print(String.format("%d ", j));
            System.out.print('\n');
        }
    }
}
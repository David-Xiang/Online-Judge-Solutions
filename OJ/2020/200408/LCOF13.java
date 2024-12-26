import java.util.ArrayDeque;
import java.util.Queue;

/**
 * LeetCodeOffer 13 Medium
 * Range of Robot
 * BFS
 */

public class LCOF13 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.movingCount(2, 3, 1)); // return 3
        System.out.println(solution.movingCount(3, 1, 0)); // return 1
        System.out.println(solution.movingCount(3, 2, 17)); // return 6

    }

    static
    class Solution {
        public int movingCount(int m, int n, int k) {
            if (m <= 0 || n <= 0) {
                return 0;
            }

            boolean [][] visited = new boolean[m][n];
            int [][] dir = new int [][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            int count = 0;

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    visited[i][j] = false;
                }
            }

            Queue<Coordinate> queue = new ArrayDeque<>();
            queue.add(new Coordinate(0, 0));
            visited[0][0] = true;
            while(!queue.isEmpty()) {
                Coordinate c = queue.remove();
                if (numSum(c.r) + numSum(c.c) <= k) {
                    count += 1;
                    for (int i = 0; i < 4; i++) {
                        int row = c.r + dir[i][0];
                        int col = c.c + dir[i][1];
                        if (in(row, col, m, n) && !visited[row][col]){
                            visited[row][col] = true;
                            queue.add(new Coordinate(row, col));
                        }
                    }
                }
            }
            return count;
        }
        static class Coordinate {
            int r, c;
            Coordinate(int r, int c){
                this.r = r;
                this.c = c;
            }
        }
        private int numSum(int n) {
            int sum = 0;
            while (n != 0) {
                sum += n % 10;
                n /= 10;
            }
            return sum;
        }
        private boolean in(int r, int c, int m, int n) {
            return r < m && r >= 0 && c < n && c >= 0;
        }
    }
}
/**
 * LeetCode 289 Medium
 * Game of Life
 * Bit Manipulation
 * 扩散模型，位运算实现in-place计算
 */

public class LC289 {
    public static void main(String [] args){
        int [][] board = {
                {0, 1, 0},
                {0, 0, 1},
                {1, 1, 1},
                {0, 0, 0}
        };
        Solution solution = new Solution();
        solution.gameOfLife(board);
        int h = board.length;
        int w = board[0].length;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
    }

    static
    class Solution {
        public void gameOfLife(int[][] board) {
            int [][] dir = {
                    {-1, -1},
                    {-1, 0},
                    {-1, 1},
                    {0, -1},
                    {0, +1},
                    {+1, -1},
                    {+1, 0},
                    {+1, +1}
            };
            int h = board.length;
            int w = board[0].length;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    int count = 0;
                    for (int k = 0; k < 8; k++) {
                        if (!inBound(h, w, i+dir[k][0], j+dir[k][1])){
                            continue;
                        }
                        count += (board[i+dir[k][0]][j+dir[k][1]] & 1);
                    }
                    if (count == 2 && (board[i][j] & 1) == 1) {
                        // live -> live
                        board[i][j] = (board[i][j] | 2);
                    } else if (count == 3){
                        // live, died -> live
                        board[i][j] = (board[i][j] | 2);
                    }
                }
            }
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    board[i][j] = board[i][j] >> 1;
                }
            }
        }
        boolean inBound(int h, int w, int x, int y) {
            return x >= 0 && x < h && y >= 0 && y < w;
        }
    }
}
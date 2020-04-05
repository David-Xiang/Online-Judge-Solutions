/**
 * LeetCode 1025 Easy
 * Divisor Game
 * Dynamic Programming
 */

public class LC1025 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.divisorGame(2));
        System.out.println(solution.divisorGame(3));
        System.out.println(solution.divisorGame(4));
    }

    static
    class Solution {
        public boolean divisorGame(int N) {
            boolean [] win = new boolean [N+1];
            win[1] = false;
            for (int i = 2; i <= N; i++) {
                win[i] = false;
                for (int j = 1; j * j <= i; j++) {
                    if (i % j == 0 && !win[i - j]) {
                        win[i] = true;
                        break;
                    }
                }
            }
            return win[N];
        }
    }
}
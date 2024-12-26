/**
 * LeetCodeOffer 10-II Easy
 * Climbing Stairs
 */

public class LCOF10II {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.numWays(7));
    }

    static
    class Solution {
        public int numWays(int n) {
            if (n == 0) {
                return 1;
            }
            int a = 1, b = 1;
            for (int i = 1; i < n; i++) {
                int tmp = b;
                b = (b + a) % 1000000007;
                a = tmp;
            }
            return b;
        }
    }
}
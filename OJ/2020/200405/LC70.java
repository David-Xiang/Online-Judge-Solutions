/**
 * LeetCode 70 Easy
 * Climbing Stairs
 */

public class LC70 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.climbStairs(3));
    }

    static
    class Solution {
        public int climbStairs(int n) {
            if (n < 2)
                return 1;
            int a = 1, b = 1, res = 0;
            for (int i = 2; i <= n; i++) {
                res = a + b;
                a = b;
                b = res;
            }
            return res;
        }
    }
}
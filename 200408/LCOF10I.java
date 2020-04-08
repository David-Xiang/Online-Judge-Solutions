/**
 * LeetCodeOffer 10-I Easy
 * Fibonacci
 */

public class LCOF10I {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.fib(95));
    }

    static
    class Solution {
        public int fib(int n) {
            if (n == 0) {
                return 0;
            }
            int a = 0, b = 1;
            for (int i = 1; i < n; i++) {
                int tmp = b;
                b = (b + a) % 1000000007;
                a = tmp;
            }
            return b;
        }
    }
}
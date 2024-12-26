/**
 * LeetCode 123 Hard
 * Best Time to Buy and Sell Stock III
 * Dynamic Programming
 */

public class LC123 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int[] {3,3,5,0,0,3,1,4}));
        System.out.println(solution.maxProfit(new int[] {1,2,3,4,5}));
        System.out.println(solution.maxProfit(new int[] {7,6,4,3,1}));
    }

    static
    class Solution {
        public int maxProfit(int[] prices) {
            if (prices.length < 2) {
                return 0;
            }
            int MIN_VALUE = -1000000; // 不能赋成Integer.MIN_VALUE，会溢出
            int [][] dp =  {{0, MIN_VALUE}, {MIN_VALUE, -prices[0]}, {MIN_VALUE, MIN_VALUE}};
            // 第一位表示买入次数，第二位表示是否持有
           for (int t = 1; t < prices.length; t++) {
               for (int k = 2; k >= 1; k--) {
                   dp[k][0] = Math.max(dp[k][0], dp[k][1] + prices[t]);
                   dp[k][1] = Math.max(dp[k][1], dp[k-1][0] - prices[t]);
               }
           }
           int res = 0;
           for (int i = 0; i <= 2; i++) {
               res = Math.max(res, dp[i][0]);
           }
           return res;
        }
    }
}
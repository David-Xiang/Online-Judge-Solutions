/**
 * LeetCode 188 Hard
 * Best Time to Buy and Sell Stock IV
 * Dynamic Programming
 */

public class LC188 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(2, new int[] {2,4,1}));
        System.out.println(solution.maxProfit(2, new int[] {3,2,6,5,0,3}));
    }

    static
    class Solution {
        public int maxProfit(int maxRound, int[] prices) {
            if (prices.length < 2 || maxRound < 1) {
                return 0;
            }
            int MIN_VALUE = -1000000; // 不能赋成Integer.MIN_VALUE，会溢出
            maxRound = Math.min(maxRound, prices.length / 2); // 不加这句会爆内存
            int [][] dp = new int [maxRound+1][2];
            for (int i = 0; i <= maxRound; i++) {
                dp[i][0] = MIN_VALUE;
                dp[i][1] = MIN_VALUE;
            }
            dp[0][0] = 0;
            dp[1][1] = -prices[0];
            // 第一位表示买入次数，第二位表示是否持有
            for (int t = 1; t < prices.length; t++) {
                for (int k = maxRound; k >= 1; k--) {
                    dp[k][0] = Math.max(dp[k][0], dp[k][1] + prices[t]);
                    dp[k][1] = Math.max(dp[k][1], dp[k-1][0] - prices[t]);
                }
            }
            int res = 0;
            for (int i = 0; i <= maxRound; i++) {
                res = Math.max(res, dp[i][0]);
            }
            return res;
        }
    }
}
/**
 * LeetCode 309 Hard
 * Best Time to Buy and Sell Stock with Cooldown
 * Dynamic Programming
 */

public class LC309 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int[] {1,2,3,0,2}));
    }

    static
    class Solution {
        public int maxProfit(int[] prices) {
            if (prices.length < 2) {
                return 0;
            }
            int maxHoldPrev = -prices[0];
            int maxSoldPrev = 0;
            int maxSoldPrevPrev = 0;
            for (int i = 1; i < prices.length; i++) {
                int hold = Math.max(maxHoldPrev, maxSoldPrevPrev - prices[i]);
                int sold = Math.max(maxSoldPrev, maxHoldPrev + prices[i]);
                maxHoldPrev = hold;
                maxSoldPrevPrev = maxSoldPrev;
                maxSoldPrev = sold;
            }
            return maxSoldPrev;
        }
    }
}
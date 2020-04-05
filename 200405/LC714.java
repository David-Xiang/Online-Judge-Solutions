/**
 * LeetCode 714 Medium
 * Best Time to Buy and Sell Stock with Transaction Fee
 * Dynamic Programming
 */

public class LC714 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int[] {1, 3, 2, 8, 4, 9}, 2));
    }

    static
    class Solution {
        public int maxProfit(int[] prices, int fee) {
            if (prices.length < 2) {
                return 0;
            }
            int maxHoldPrev = -prices[0] - fee;
            int maxSoldPrev = 0;
            for (int i = 1; i < prices.length; i++) {
                int hold = Math.max(maxHoldPrev, maxSoldPrev - prices[i] - fee);
                int sold = Math.max(maxSoldPrev, maxHoldPrev + prices[i]);
                maxHoldPrev = hold;
                maxSoldPrev = sold;
            }
            return maxSoldPrev;
        }
    }
}
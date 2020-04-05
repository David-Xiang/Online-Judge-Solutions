/**
 * LeetCode 122 Easy
 * Best Time to Buy and Sell Stock II
 * Dynamic Programming
 */

public class LC122 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int [] {7,1,5,3,6,4}));
        System.out.println(solution.maxProfit(new int [] {1,2,3,4,5}));
    }

    static
    class Solution {
        public int maxProfit(int[] prices) {
            if (prices.length < 2) {
                return 0;
            }
            int maxHold = -prices[0];
            int maxSold = 0;
            for (int i = 1; i < prices.length; i++) {
                int hold = Math.max(maxHold, maxSold - prices[i]);
                int sold = Math.max(maxSold, maxHold + prices[i]);
                maxHold = hold;
                maxSold = sold;
            }
            return maxSold;
        }
    }
}
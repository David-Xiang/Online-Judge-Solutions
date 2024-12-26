/**
 * LeetCode 121 Easy
 * Best Time to Buy and Sell Stock
 * Dynamic Programming
 */

public class LC121 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.maxProfit(new int [] {7,1,5,3,6,4}));
        System.out.println(solution.maxProfit(new int [] {7,6,4,3,1}));
    }

    static
    class Solution {
        public int maxProfit(int[] prices) {
            if (prices.length < 2) {
                return 0;
            }
            int minPrice = prices[0];
            int res = 0;
            for (int i = 1; i < prices.length; i++) {
                res = Math.max(prices[i] - minPrice, res);
                minPrice = Math.min(prices[i], minPrice);
            }
            return res;
        }
    }
}
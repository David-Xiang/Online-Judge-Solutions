/**
 * LeetCode 53 Easy
 * Maximum Subarray
 * Dynamic Programming
 */

public class LC53 {
    public static void main(String [] args){
        int [] arr = {-2,1,-3,4,-1,2,1,-5,4};
        Solution solution = new Solution();
        System.out.println(solution.maxSubArray(arr));
    }

    static
    class Solution {
        public int maxSubArray(int[] nums) {
            int [] dp = new int [nums.length]; // dp[i]表示以i结尾的最大子串
            dp[0] = nums[0];
            int res = dp[0];
            for (int i = 1; i < nums.length; i++) {
                dp[i] = nums[i];
                if (dp[i-1] > 0) {
                    dp[i] += dp[i-1];
                }
                res = Math.max(res, dp[i]);
            }
            return res;
        }
    }
}
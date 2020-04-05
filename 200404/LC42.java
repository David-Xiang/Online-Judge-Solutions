/**
 * LeetCode 42 Hard
 * Trapping Rain Water
 * Dynamic Programming
 */

public class LC42 {
    public static void main(String [] args){
        int [] arr = {0,1,0,2,1,0,1,3,2,1,2,1};
        Solution solution = new Solution();
        System.out.println(solution.trap(arr)); // return 6
    }

    static
    class Solution {
        public int trap(int[] height) {
            int len = height.length;
            if (len < 3) {
                return 0;
            }
            int [] maxLeft = new int [len];
            int [] maxRight = new int [len];
            maxLeft[0] = 0;
            maxRight[len-1] = 0;
            for (int i = 1; i < len - 1; i++) {
                maxLeft[i] = Math.max(maxLeft[i-1], height[i-1]);
                maxRight[len-i-1] = Math.max(maxRight[len-i], height[len-i]);
            }
            int sum = 0;
            for (int i = 1; i < len - 1; i++) {
                if (height[i] < maxLeft[i] && height[i] < maxRight[i]) {
                    sum += Math.min(maxLeft[i], maxRight[i]) - height[i];
                }
            }
            return sum;
        }
    }
}
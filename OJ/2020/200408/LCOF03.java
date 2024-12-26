package com.xiangdongwei;

/**
 * LeetCodeOffer 03 Hardness
 * Repeated Number in Array
 */

public class LCOF03 {
    public static void main(String [] args){
        int [] arr = {2, 3, 1, 0, 2, 5, 3};
        Solution solution = new Solution();
        System.out.println(solution.findRepeatNumber(arr));
    }

    static
    class Solution {
        public int findRepeatNumber(int[] nums) {
            boolean [] find = new boolean[nums.length];
            for (int num : nums) {
                if (!find[num]) {
                    find[num] = true;
                } else {
                    return num;
                }
            }
            return 0;
        }
    }
}
/**
 * LeetCodeOffer 21 Easy
 * Exchange Even and Odd
 * Array
 * 调整数组顺序使奇数位于偶数前面
 */

public class LCOF21 {
    public static void main(String [] args){
        int [] arr = {1, 3, 2, 5};
        Solution solution = new Solution();
        int [] res = solution.exchange(arr);
        for (int i : res) {
            System.out.println(i);
        }
    }

    static
    class Solution {
        public int[] exchange(int[] nums) {
            int [] res = new int[nums.length];
            for (int i = 0, j = nums.length - 1; i <= j; ) {
                while(i <= j && nums[i] % 2 == 1) {
                    res[i] = nums[i];
                    i++;
                }
                while(i <= j && nums[j] % 2 == 0) {
                    res[j] = nums[j];
                    j--;
                }
                if (i < j) {
                    res[i] = nums[j];
                    res[j] = nums[i];
                    i++;
                    j--;
                }
            }

            return res;
        }
    }
}
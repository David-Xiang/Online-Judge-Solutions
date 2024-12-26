/**
 * LeetCode 75 Medium
 * Sort Colors
 * Three Pointers
 * 一遍扫描，排序包含012的序列
 */

public class LC75 {
    public static void main(String [] args){
        int [] arr = {2,0,2,1,1,0};
        int [] arr1 = {2,0,1};
        Solution solution = new Solution();
        solution.sortColors(arr);
        solution.sortColors(arr1);
        for (int i: arr) {
            System.out.print(i + " ");
        }
        System.out.println();
        for (int i: arr1) {
            System.out.print(i + " ");
        }
    }

    static
    class Solution {
        public void sortColors(int[] nums) {
            int zp = 0, tp = nums.length - 1, curr = 0; // 0/2的指针，和一个当前指针
            while (curr <= tp) {
                if (nums[curr] == 0) {
                    swap(nums, curr, zp);
                    curr++;
                    zp++;
                } else if (nums[curr] == 2) {
                    swap(nums, curr, tp);
                    tp--;
                } else {
                    curr++;
                }
            }
        }
        private void swap(int [] num, int ia, int ib) {
            int tmp = num[ia];
            num[ia] = num[ib];
            num[ib] = tmp;
        }
    }
}
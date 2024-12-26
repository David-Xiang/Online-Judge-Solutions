/**
 * LeetCode 215 Medium
 * Kth Largest Element in an Array
 * Divide and Conquer
 */

public class LC215 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.findKthLargest(new int [] {3,2,1,5,6,4}, 2));
        System.out.println(solution.findKthLargest(new int [] {3,2,3,1,2,4,5,5,6}, 4));
    }

    static
    class Solution {
        public int findKthLargest(int[] nums, int k) {
            return findKthLargestInternal(nums, k, 0, nums.length);
        }
        public int findKthLargestInternal(int[] nums, int k, int begin, int end) {
            int p = nums[begin];
            int i = begin, j = end - 1;
            while (i != j) {
                while(i != j && nums[j] < p) j--;
                if (i != j) nums[i++] = nums[j];
                while (i != j && nums[i] >= p) i++;
                if (i != j) nums[j--] = nums[i];
            }
            nums[i] = p;
            if (k == i + 1) {
                return p;
            } else if (k <= i) {
                return findKthLargestInternal(nums, k, begin, i);
            } else {
                return findKthLargestInternal(nums, k, i + 1, end);
            }
        }
    }
}
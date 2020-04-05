import java.util.Arrays;

/**
 * LeetCode 1 Simple
 * Two Sum
 * Array
 */

public class LC1 {
    public static void main(String [] args){
        int [] arr = {2, 5, 5, 11};
        int target = 10;
        Solution solution = new Solution();
        System.out.println(solution.twoSum(arr, target)[0] + " " + solution.twoSum(arr, target)[1]);
    }

    static
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            int [] numn = Arrays.copyOf(nums, nums.length);
            Arrays.sort(numn);
            int i = 0, j = numn.length - 1;
            while(i != j) {
                if (numn[i] + numn[j] == target) {
                    break;
                } else if (numn[i] + numn[j] < target) {
                    i++;
                } else {
                    j--;
                }
            }
            int a = numn[i], b = numn[j];
            int ia = 0, ib = 0;
            boolean founda = false;
            for (i = 0; i < nums.length; i++) {
                if (nums[i] == a && !founda) {
                    ia = i;
                    founda = true;
                } else if (nums[i] == b) {
                    ib = i;
                }
            }
            return new int [] {ia, ib};
        }
    }
}
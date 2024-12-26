public class LC303 {
    public static void main(String [] args){
        int [] nums = {-2, 0, 3, -5, 2, -1};
        NumArray array = new NumArray(nums);
        System.out.println(array.sumRange(0, 2)); // 1
        System.out.println(array.sumRange(2, 5)); // -1
        System.out.println(array.sumRange(0, 5)); // -3
    }

    static
    class NumArray {
        int [] sum;
        public NumArray(int[] nums) {
            sum = new int [nums.length+1];
            sum[0] = 0;
            for (int i = 1; i <= nums.length; i++) {
                sum[i] = sum[i-1] + nums[i-1];
            }
        }

        public int sumRange(int i, int j) {
            return sum[j+1] - sum[i];
        }
    }
}
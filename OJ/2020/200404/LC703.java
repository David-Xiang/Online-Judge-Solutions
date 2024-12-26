/**
 * LeetCode 703 Easy
 * Kth Largest Element in a Stream
 * Heap
 * 维护一个大小为k的小根堆，保存最大的k个数，堆顶就是答案
 * 需要注意初始数组大小可能不足k
 */

public class LC703 {
    public static void main(String [] args){
        int [] arr = {4,5,8,2};
        KthLargest kthLargest = new KthLargest(3, arr);
        System.out.println(kthLargest.add(3)); // returns 4
        System.out.println(kthLargest.add(5)); // returns 5
        System.out.println(kthLargest.add(10)); // returns 5
        System.out.println(kthLargest.add(9)); // returns 8
        System.out.println(kthLargest.add(4)); // returns 8
        kthLargest = new KthLargest(7, new int [] {-10,1,3,1,4,10,3,9,4,5,1});
        System.out.println(kthLargest.add(3)); // returns 3
        System.out.println(kthLargest.add(2)); // returns 3
        System.out.println(kthLargest.add(3)); // returns 3
        System.out.println(kthLargest.add(1)); // returns 3
        System.out.println(kthLargest.add(2)); // returns 3
        System.out.println(kthLargest.add(4)); // returns 3
    }

    static
    class KthLargest {
        private int [] val;
        private int len;
        public KthLargest(int k, int[] nums) {
            val = new int [k];
            len = Math.min(k, nums.length);
            System.arraycopy(nums, 0, val, 0, len);
            heapify();
            for (int i = len; i < nums.length; i++) {
                add(nums[i]);
            }
        }

        public int add(int n) {
            if (n <= val[0] && len == val.length) {
                return val[0];
            }
            if (len == val.length) {
                val[0] = n;
                siftDown(0);
            } else {
                val[len++] = n;
                siftUp(len-1);
            }

            return val[0];
        }
        
        private void heapify() {
            int nodes = len / 2 - 1;
            for (int i = nodes ; i >= 0; i--) {
                siftDown(i);
            }
        }

        private void siftDown(int i) {
            int j = 2 * i + 1;
            if (j >= len) {
                return;
            }

            if (j + 1 < len && val[j+1] < val[j]) {
                j = j + 1;
            }
            if (val[i] > val[j]) {
                swap(i, j);
                siftDown(j);
            }
        }

        private void siftUp(int i) {
            if (i == 0) {
                return;
            }
            int j = (i - 1) / 2;
            if (val[j] > val[i]) {
                swap(i, j);
                siftUp(j);
            }
        }

        private void swap(int ia, int ib) { int tmp = val[ia]; val[ia] = val[ib]; val[ib] = tmp; }
    }
}
public class Heap {
    // 最小堆
    private int [] val;
    private int len;
    public static void main(String [] args){
        int [] arr = {4,5,8,2};
        Heap heap = new Heap(10, arr);
        heap.push(1);
        heap.pop();
        heap.push(1);
        heap.push(0);
        heap.pop();
        heap.pop();
        heap.push(10);
        heap.push(1);
        heap.push(2);
        heap.pop();
        heap.pop();
        heap.pop();
    }
    public Heap(int k, int[] nums) {
        // k表示堆最大容量，假设不会超过
        val = new int [k];
        len = nums.length;
        System.arraycopy(nums, 0, val, 0, len);
        heapify();
    }

    public void push(int n) {
        val[len++] = n;
        siftUp(len-1);
    }

    public int pop() {
        int top = val[0];
        val[0] = val[--len];
        siftDown(0);

        return top;
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

    private void swap(int ia, int ib) {
        int tmp = val[ia];
        val[ia] = val[ib];
        val[ib] = tmp;
    }
}

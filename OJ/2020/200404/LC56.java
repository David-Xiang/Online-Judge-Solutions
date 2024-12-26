/**
 * LeetCode 56 Medium
 * Merge Intervals
 * Sort
 */

public class LC56 {
    public static void main(String [] args){
        int [][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        Solution solution = new Solution();
        int [][] merged = solution.merge(intervals);
        for (int[] ints : merged) {
            System.out.printf("(%d, %d)\n", ints[0], ints[1]);
        }
    }

    static
    class Solution {
        public int[][] merge(int[][] val) {
            if (val.length == 0){
                return new int[0][2];
            }
            sort(val, 0, val.length);
            int count = 1;
            int last = val[0][1];
            for (int i = 1; i < val.length; i++) {
                if (val[i][0] > last) {
                    count++;
                }
                last = Math.max(last, val[i][1]);
            }

            int [][] res = new int[count][2];
            res[0][0] = val[0][0];
            last = val[0][1];
            count = 0;
            for (int i = 1; i < val.length; i++) {
                if (val[i][0] > last) {
                    res[count++][1] = last;
                    res[count][0] = val[i][0];
                }
                last = Math.max(last, val[i][1]);
            }
            res[count][1] = last;
            return res;
        }
        public void sort(int[][] val, int begin, int end) {
            if (begin + 1 >= end) {
                return;
            }
            int p = val[begin][0];
            int p1 = val[begin][1];
            int i = begin, j = end - 1;
            while (i != j) {
                while(i != j && val[j][0] > p) j--;
                if (i != j) {
                    val[i][0] = val[j][0];
                    val[i][1] = val[j][1];
                }
                while(i != j && val[i][0] <= p) i++;
                if (i != j) {
                    val[j][0] = val[i][0];
                    val[j][1] = val[i][1];
                }
            }
            val[i][0] = p;
            val[i][1] = p1;
            sort(val, begin, i);
            sort(val, i + 1, end);
        }
    }
}
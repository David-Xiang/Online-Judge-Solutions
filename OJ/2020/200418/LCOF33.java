/**
 * LeetCodeOffer 33 Medium
 * Verify Postorder
 * Tree
 */

public class LCOF33 {
    public static void main(String [] args){
        Solution solution = new Solution();
        System.out.println(solution.verifyPostorder(new int[] {1,6,3,2,5})); // false
        System.out.println(solution.verifyPostorder(new int[] {1,3,2,6,5})); // true
        System.out.println(solution.verifyPostorder(new int[] {5,4,3,2,1})); // true
    }

    static
    class Solution {
        public boolean verifyPostorder(int[] postorder) {
            return verifyPostorderInternal(postorder, 0, postorder.length);
        }
        private boolean verifyPostorderInternal(int[] postorder, int begin, int end) {
            if (end < begin + 3) {
                return true;
            }
            int p = postorder[end - 1];
            int i;
            for (i = begin; i < end - 1; i++) {
                if (postorder[i] > p) break;
            }
            for (int j = i; j < end - 1; j++) {
                if (postorder[j] < p)
                    return false;
            }
            return verifyPostorderInternal(postorder, begin, i) &&
                    verifyPostorderInternal(postorder, i, end - 1);
        }
    }
}
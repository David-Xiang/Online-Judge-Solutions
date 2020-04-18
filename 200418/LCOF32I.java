import java.util.*;

/**
 * LeetCodeOffer 32-I Medium
 * Print Tree in Level Order
 * Tree
 */

public class LCOF32I {
    public static void main(String [] args){
        Solution solution = new Solution();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        int [] res = solution.levelOrder(root);
        for (int i : res) {
            System.out.println(i);
        }
    }

    static
    class Solution {
        public int[] levelOrder(TreeNode root) {
            if (root == null) {
                return new int[0];
            }
            List<Integer> arr = new ArrayList<>();
            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            while (queue.peek() != null) {
                TreeNode t = queue.remove();
                arr.add(t.val);
                if (t.left != null) {
                    queue.add(t.left);
                }
                if (t.right != null) {
                    queue.add(t.right);
                }
            }
            int[] res = new int[arr.size()];
            for (int i = 0; i < arr.size(); i++) {
                res[i] = arr.get(i);
            }
            return res;
        }
    }

    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int x) {
            val = x;
        }
    }
}
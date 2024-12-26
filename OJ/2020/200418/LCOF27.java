/**
 * LeetCodeOffer 27 Easy
 * Invert Binary Tree
 * Tree
 */

public class LCOF27 {
    public static void main(String [] args){
        TreeNode t1 = new TreeNode(1);
        t1.left = new TreeNode(2);
        t1.right = new TreeNode(3);
        t1.left.left = new TreeNode(4);
        t1.left.right = new TreeNode(5);
        t1.right.left = new TreeNode(6);
        t1.right.right = new TreeNode(7);
        Solution solution = new Solution();
        solution.mirrorTree(t1);
        System.out.println(t1);
    }

    static
    class Solution {
        public TreeNode mirrorTree(TreeNode root) {
            if (root == null) {
                return root;
            }
            TreeNode t = root.left;
            root.left = root.right;
            root.right = t;
            if (root.left != null) {
                mirrorTree(root.left);
            }
            if (root.right != null) {
                mirrorTree(root.right);
            }
            return root;
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
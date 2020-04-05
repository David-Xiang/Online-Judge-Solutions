/**
 * LeetCode 965 Easy
 * Univalued Binary Tree
 * Tree
 */

public class LC965 {
    public static void main(String [] args){
        TreeNode root = new TreeNode(2);
        root.left = new TreeNode(2);
        root.right = new TreeNode(5);
        Solution solution = new Solution();
        System.out.println(solution.isUnivalTree(root));
    }

    static
    class Solution {
        public boolean isUnivalTree(TreeNode root) {
            boolean leftUnival = root.left == null || (root.val == root.left.val && isUnivalTree(root.left));
            boolean rightUnival = root.right == null || (root.val == root.right.val && isUnivalTree(root.right));
            return leftUnival && rightUnival;
        }
    }

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) {
            val = x;
        }
    }
}
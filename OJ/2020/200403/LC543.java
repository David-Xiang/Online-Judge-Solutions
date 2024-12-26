/**
 * LeetCode 543 Easy
 * Diameter of Binary Tree
 * Tree Traversal
 */

public class LC543 {
    public static void main(String [] args){
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(3);
        root.left = new TreeNode(2);
        root.left.right = new TreeNode(5);
        root.left.left = new TreeNode(4);
        Solution solution = new Solution();
        System.out.println(solution.diameterOfBinaryTree(root));
    }

    static
    class Solution {
        public int diameterOfBinaryTree(TreeNode root) {
            if (root == null) {
                return 0;
            }
            return Math.max(
                    Math.max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right)),
                    radiusOfBinaryTree(root.left) + radiusOfBinaryTree(root.right) + 2
            );
        }
        public int radiusOfBinaryTree(TreeNode root) {
            if (root == null) {
                return -1;
            }
            return Math.max(radiusOfBinaryTree(root.right) + 1, radiusOfBinaryTree(root.left) + 1);
        }
    }
    static public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}
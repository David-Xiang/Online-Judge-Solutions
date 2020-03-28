import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * LeetCode 144 Medium
 * Binary Tree Preorder Traversal
 * Tree
 */

public class LC144{
    public static void main(String [] args){
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);
        one.right = two;
        two.left = three;
        Solution solution = new Solution();
        System.out.println(solution.preorderTraversal(one));
    }

    static
    class Solution {
        public List<Integer> preorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();

            stack.push(root);
            while(!stack.empty()) {
                TreeNode curr = stack.pop();
                if (curr == null) {
                    continue;
                }
                result.add(curr.val);
                if (curr.right != null) {
                    stack.push(curr.right);
                }
                if (curr.left != null) {
                    stack.push(curr.left);
                }
            }
            return result;
        }
    }

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}
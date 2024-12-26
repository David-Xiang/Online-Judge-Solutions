import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * LeetCode 145 Hard
 * Binary Tree PostOrder Traversal
 * Tree
 */

public class LC145 {
    public static void main(String [] args){
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);
        one.right = two;
        two.left = three;
        Solution solution = new Solution();
        System.out.println(solution.postorderTraversal(one));
    }

    static
    class Solution {
        public List<Integer> postorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            Stack<StackItem> stack = new Stack<>();

            stack.push(new StackItem(root, 0));
            while(!stack.empty()) {
                StackItem curr = stack.pop();

                if (curr.node == null) {
                    continue;
                }

                if (curr.countSeen == 0) {
                    curr.countSeen = 1;
                    stack.push(curr);
                    if (curr.node.left != null) {
                        stack.push(new StackItem(curr.node.left, 0));
                    }
                } else if (curr.countSeen == 1) {
                    curr.countSeen = 2;
                    stack.push(curr);
                    if (curr.node.right != null) {
                        stack.push(new StackItem(curr.node.right, 0));
                    }
                } else {
                    result.add(curr.node.val);
                }
            }
            return result;
        }

        static class StackItem {
            TreeNode node;
            int countSeen;
            StackItem(TreeNode t, int n) {
                node = t;
                countSeen = n;
            }
        }
    }

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}
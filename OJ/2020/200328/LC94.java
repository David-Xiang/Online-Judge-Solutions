import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * LeetCode 94 Medium
 * Binary Tree Inorder Traversal
 * Tree
 */

public class LC94{
    public static void main(String [] args){
        TreeNode one = new TreeNode(1);
        TreeNode two = new TreeNode(2);
        TreeNode three = new TreeNode(3);
        one.right = two;
        two.left = three;
        Solution solution = new Solution();
        System.out.println(solution.inorderTraversal(null));
    }

    static
    class Solution {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            Stack<StackItem> stack = new Stack<>();

            stack.push(new StackItem(root, true));
            while(!stack.empty()) {
                StackItem curr = stack.pop();

                if (curr.node == null) {
                    continue;
                }

                if (curr.firstSeen) {
                    curr.firstSeen = false;
                    stack.push(curr);
                    if (curr.node.left != null) {
                        stack.push(new StackItem(curr.node.left, true));
                    }
                } else {
                    result.add(curr.node.val);
                    if (curr.node.right != null) {
                        stack.push(new StackItem(curr.node.right, true));
                    }
                }
            }
            return result;
        }

        static class StackItem {
            TreeNode node;
            boolean firstSeen;
            StackItem(TreeNode n, boolean b) {
                node = n;
                firstSeen = b;
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
import java.util.*;

/**
 * LeetCodeOffer 32-III Medium
 * Print Tree in Level Order
 * Tree
 */

public class LCOF32III {
    public static void main(String [] args){
        Solution solution = new Solution();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        List<List<Integer>> res = solution.levelOrder(root);
        for (List<Integer> list: res) {
            for (int i : list) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }

    static
    class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
            if (root == null) {
                return new ArrayList<>();
            }
            List<List<Integer>> res = new ArrayList<>();

            Stack<TreeNode> thisLevel = new Stack<>(), nextLevel = new Stack<>();
            int level = 1;
            thisLevel.add(root);
            List<Integer> list = new ArrayList<>();
            while (!thisLevel.empty()) {
                while(!thisLevel.empty()) {
                    TreeNode t = thisLevel.pop();
                    list.add(t.val);
                    if (level % 2 == 1) {
                        if (t.left != null) {
                            nextLevel.push(t.left);
                        }
                        if (t.right != null) {
                            nextLevel.push(t.right);
                        }
                    } else {
                        if (t.right != null) {
                            nextLevel.push(t.right);
                        }
                        if (t.left != null) {
                            nextLevel.push(t.left);
                        }
                    }
                }
                level++;
                thisLevel = nextLevel;
                nextLevel = new Stack<>();
                res.add(list);
                list = new ArrayList<>();
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
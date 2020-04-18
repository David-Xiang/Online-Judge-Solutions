import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * LeetCodeOffer 32-II Medium
 * Print Tree in Level Order
 * Tree
 */

public class LCOF32II {
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

            Queue<TreeNode> queue = new LinkedList<>();
            queue.add(root);
            List<Integer> list = new ArrayList<>();
            int len = 1, lenNext = 0, count = 0;
            while (queue.peek() != null) {
                TreeNode t = queue.remove();
                list.add(t.val);
                count++;
                if (t.left != null) {
                    queue.add(t.left);
                    lenNext++;
                }
                if (t.right != null) {
                    queue.add(t.right);
                    lenNext++;
                }
                if (count == len) {
                    res.add(list);
                    list = new ArrayList<>();
                    count = 0;
                    len = lenNext;
                    lenNext = 0;
                }
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
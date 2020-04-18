/**
 * LeetCodeOffer 26 Easy
 * Substructure of a Tree
 * Tree
 */

public class LCOF26 {
    public static void main(String [] args){
        TreeNode t1 = new TreeNode(3);
        t1.right = new TreeNode(5);
        t1.left = new TreeNode(4);
        t1.left.right = new TreeNode(2);
        t1.left.left = new TreeNode(1);
        TreeNode t2 = new TreeNode(4);
        t2.left = new TreeNode(1);
        System.out.println(new Solution().isSubStructure(t1, t2));
        System.out.println(new Solution().isSubStructure(t1.left, t2));
    }

    static
    class Solution {
        public boolean isSubStructure(TreeNode A, TreeNode B) {
            return equalsExistingPart(A, B) || (A.left != null && isSubStructure(A.left, B)) || (A.right != null && isSubStructure(A.right, B));
        }
        public boolean equalsExistingPart(TreeNode A, TreeNode B) { // 在非null部分 相等即可
            if (A == null || B == null) {
                return false;
            }
            return A.val == B.val && (B.left == null || equalsExistingPart(A.left, B.left)) && (B.right == null || equalsExistingPart(A.right, B.right));
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
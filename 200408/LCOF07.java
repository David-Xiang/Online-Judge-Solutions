/**
 * LeetCodeOffer 07 Medium
 * Construct Binary Tree from Preorder and Inorder Traversal
 * Tree
 * 类似树重建或者分治排序（快排、归并）所用的index最好是针对原数组的绝对index
 * 不容易出错
 */

public class LCOF07 {
    public static void main(String [] args){
//        int [] preorder = {3,9,20,15,7};
//        int [] inorder = {9,3,15,20,7};
        int [] preorder = {1,2,3};
        int [] inorder = {2,3,1};
        Solution solution = new Solution();
        TreeNode root = solution.buildTree(preorder, inorder);
        System.out.println(root.val);
    }

    static
    class Solution {
        public TreeNode buildTree(int[] preorder, int[] inorder) {
            if (preorder.length == 0) {
                return null;
            }
            return buildTreeInternal(preorder, 0, inorder,0, preorder.length);
        }
        private TreeNode buildTreeInternal(int[] preorder, int pstart, int[] inorder, int istart, int length) {
            if (length <= 0) return null;
            int val = preorder[pstart];
            TreeNode root = new TreeNode(val);
            int index;
            for (index = 0; index < length; index++) {
                if (inorder[istart+index] == val)
                    break;
            }
            root.left = buildTreeInternal(preorder, pstart + 1, inorder, istart, index);
            root.right = buildTreeInternal(preorder, pstart + index + 1, inorder, istart + index + 1, length - index - 1);
            return root;
        }
    }

    static
    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
}
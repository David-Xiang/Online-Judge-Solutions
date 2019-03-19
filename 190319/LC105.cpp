// LeetCode 105
// Construct Binary Tree from Preorder and Inorder Traversal
// preorder = [3,9,20,15,7]
// inorder = [9,3,15,20,7]

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return buildSubTree(preorder, inorder, 0, preorder.size(), 0, inorder.size());
    }
    TreeNode* buildSubTree(vector<int>& preorder, vector<int>& inorder, int pl, int pr, int il, int ir){
        if (pl == pr)
            return NULL;
        int rootVal = preorder[pl];
        TreeNode* root = new TreeNode(rootVal);
        int id = 0;
        for (id = 0; id < ir - il; id++)
            if (inorder[il + id] == rootVal)
                break;
        if (id > 0)
            root->left = buildSubTree(preorder, inorder, pl+1, pl+id+1, il, il+id);
        if (id < ir - il - 1)
            root->right = buildSubTree(preorder, inorder, pl+id+1, pr, il+id+1, ir);
        return root;
    }
};
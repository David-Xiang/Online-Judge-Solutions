// LC 426
// Convert Binary Search Tree to Sorted Doubly Linked List
// Mock from nowcoder.com
// NOTE: be careful with pointer conversion!

/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/
 
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
        TreeNode* leftmost=NULL, *rightmost=NULL;
        if (pRootOfTree != NULL){
            ConvertInOrder(pRootOfTree, &leftmost, &rightmost);
            return leftmost;
        } else
            return pRootOfTree;
    }
    void ConvertInOrder(TreeNode* root, TreeNode** leftmost, TreeNode** rightmost){
        TreeNode *ll=NULL, *lr=NULL, *rl=NULL, *rr=NULL;
        if (root->left!=NULL){
            ConvertInOrder(root->left, &ll, &lr);
            lr->right = root;
            root->left = lr;
            *leftmost = ll;
        } else {
            *leftmost = root;
        }
        if (root->right!=NULL){
            ConvertInOrder(root->right, &rl, &rr);
            rl->left = root;
            root->right = rl;
            *rightmost = rr;
        } else {
            *rightmost = root;
        }
    }
};
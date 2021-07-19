# LeetCodeOffer 68-II
# Lowest Common Ancestor of a Binary Tree
# Tree

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None: 
            return right
        if right is None:
            return left
        return root

if __name__ == "__main__":
    val = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    nodes = [TreeNode(val[i]) for i in range(9)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    nodes[4].left = nodes[7]
    nodes[4].right = nodes[8]
    print(Solution().lowestCommonAncestor(nodes[0], nodes[1], nodes[2]).val)
    print(Solution().lowestCommonAncestor(nodes[0], nodes[1], nodes[3]).val)
    print(Solution().lowestCommonAncestor(nodes[0], nodes[3], nodes[7]).val)
    
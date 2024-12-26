# LeetCode 98
# Validate Binary Tree
# Tree

from typing import List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)[0]

    def check(self, root):
        if root is None:
            return (True, sys.maxsize, -sys.maxsize)
        left_valid, left_min, left_max = self.check(root.left)
        right_valid, right_min, right_max = self.check(root.right)
        return (
            left_valid and right_valid and left_max < root.val < right_min,
            min(left_min, root.val),
            max(right_max, root.val)
        ) 

if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(Solution().isValidBST(root1))
    print(Solution().isValidBST(root2))
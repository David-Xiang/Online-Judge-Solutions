# LeetCode 101
# Symmetric Tree
# Tree

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right, right.left)
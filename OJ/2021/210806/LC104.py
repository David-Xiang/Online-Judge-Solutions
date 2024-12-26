# LeetCode 104
# Maximum Depth of Binary Tree
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
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]
    print(Solution().maxDepth(nodes[0]))
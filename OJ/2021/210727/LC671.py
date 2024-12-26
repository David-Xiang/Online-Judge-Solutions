# LeetCode 671
# Second Minimum Node In a Binary Tree
# Tree

from typing import List
import collections
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = self.help(root)
        return ans if ans < sys.maxsize else -1

    def help(self, root): 
        if root.left is None:
            left_min = sys.maxsize
        else:
            left_min = root.left.val if root.left.val > root.val else self.help(root.left)
        if root.right is None:
            right_min = sys.maxsize
        else:
            right_min = root.right.val if root.right.val > root.val else self.help(root.right)
        
        return min(left_min, right_min)

if __name__ == "__main__":
    vals = [2, 2, 5, 5, 7]
    nodes = [TreeNode(vals[i]) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]
    print(Solution().findSecondMinimumValue(nodes[0]))

    vals = [2, 2, 2]
    nodes = [TreeNode(vals[i]) for i in range(3)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    print(Solution().findSecondMinimumValue(nodes[0]))
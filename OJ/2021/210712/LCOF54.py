# LeetCodeOffer 54
# Kth Largest Node in Binary Search Tree
# Binary Search Tree

from typing import List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    min_num = -sys.maxsize - 1

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.ans = self.min_num
        self.count = k
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if self.ans > self.min_num or root is None:
            return
        self.dfs(root.right)
        self.count = self.count - 1
        if self.count == 0:
            self.ans = root.val
        self.dfs(root.left)

def test1():
    nodes = [TreeNode(i) for i in range(5)]
    nodes[3].left = nodes[1]
    nodes[3].right = nodes[4]
    nodes[1].right = nodes[2]
    print(Solution().kthLargest(nodes[3], 1))

def test2():
    nodes = [TreeNode(i) for i in range(7)]
    nodes[5].left = nodes[3]
    nodes[5].right = nodes[6]
    nodes[3].left = nodes[2]
    nodes[3].right = nodes[4]
    nodes[2].left = nodes[1]
    print(Solution().kthLargest(nodes[5], 3))

if __name__ == "__main__":
    test1()
    test2()
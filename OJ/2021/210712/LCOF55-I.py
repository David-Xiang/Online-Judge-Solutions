# LeetCodeOffer 55-I
# Maximum Depth of Binary Tree
# Tree

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        

def test1():
    nodes = [TreeNode(i) for i in range(5)]
    nodes[3].left = nodes[1]
    nodes[3].right = nodes[4]
    nodes[1].right = nodes[2]
    print(Solution().maxDepth(nodes[3]))

def test2():
    nodes = [TreeNode(i) for i in range(7)]
    nodes[5].left = nodes[3]
    nodes[5].right = nodes[6]
    nodes[3].left = nodes[2]
    nodes[3].right = nodes[4]
    nodes[2].left = nodes[1]
    print(Solution().maxDepth(nodes[5]))

if __name__ == "__main__":
    test1()
    test2()
# LeetCode 111
# Minimum Depth of Binary Tree
# BFS

from typing import List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = collections.deque()
        q.append(root)
        depth = 1
        while len(q) > 0:
            l = len(q)
            for i in range(l):
                elem = q.popleft()
                if elem.left is None and elem.right is None:
                    return depth
                if elem.left is not None:
                    q.append(elem.left)
                if elem.right is not None:
                    q.append(elem.right)
            depth = depth + 1
        return -1

if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(6)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[4].right = nodes[5]
    print(Solution().minDepth(nodes[0]))
    print(Solution().minDepth(nodes[1]))
    print(Solution().minDepth(nodes[2]))
# LeetCode 102
# Binary Tree Level Order Traversal
# Binary Tree

from typing import List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        import collections
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            level_ans = []
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                level_ans.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(level_ans)
        return ans
    
        
if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[2].left = nodes[3]
    nodes[2].right = nodes[4]
    print(Solution().levelOrder(nodes[0]))
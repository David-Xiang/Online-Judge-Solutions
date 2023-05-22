# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None:
            return None
        return self.dfs(root, 0, limit)

    def dfs(self, node: TreeNode, sum: int, limit: int):
        sum = sum + node.val
        if node.left is None and node.right is None:
            if sum < limit:
                return None
            return node
        if node.left is not None:
            node.left = self.dfs(node.left, sum, limit)
        if node.right is not None:
            node.right = self.dfs(node.right, sum, limit)
        if node.left is None and node.right is None:
            return None
        return node


def test1():
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(-99, TreeNode(-99), TreeNode(-99))),
                    TreeNode(3, TreeNode(-99, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(-99), TreeNode(14))))
    print(Solution().sufficientSubset(root, 1))


if __name__ == "__main__":
    test1()

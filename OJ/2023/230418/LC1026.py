# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root)[2]

    def dfs(self, root: TreeNode) -> List[int]:
        vmax, vmin, vans = root.val, root.val, 0
        if root.left is not None:
            lmax, lmin, lans = self.dfs(root.left)
            vmax = max(vmax, lmax)
            vmin = min(vmin, lmin)
            vans = max(vans, lans)
        if root.right is not None:
            rmax, rmin, rans = self.dfs(root.right)
            vmax = max(vmax, rmax)
            vmin = min(vmin, rmin)
            vans = max(vans, rans)
        vans = max(vans, vmax - root.val, root.val - vmin)
        return vmax, vmin, vans

if __name__ == '__main__':
    print(Solution().maxAncestorDiff(TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, TreeNode(14, TreeNode(13))))))
    print(Solution().maxAncestorDiff(TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))))
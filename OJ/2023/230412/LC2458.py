# LeetCode 2458
# Height of Binary Tree After Subtree Removal Queries
# Tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        size = self.size(root)
        father: List[int] = [0 for _ in range(size + 1)]
        height: List[int] = [-1 for _ in range(size + 1)]
        nodes: List[TreeNode] = [TreeNode() for _ in range(size + 1)]
        memo: List[int] = [-1 for _ in range(size + 1)]

        if root is None:
            return []
            
        self.index(root, father, height, nodes)
        
        ans = []
        for q in queries:
            cur = q
            h = 0
            noImpact = False
            useMemo = False
            while father[cur] != 0:
                h = h + 1
                f = father[cur]
                fnode = nodes[f] 
                if memo[fnode.val] = 
                if fnode.left is not None and fnode.left.val != cur:
                    h = max(h, height[fnode.left.val] + 1)
                if fnode.right is not None and fnode.right.val != cur:
                    h = max(h, height[fnode.right.val] + 1)
                if h == height[fnode.val]:
                    noImpact = True
                    break
                cur = fnode.val
            memo[q] = height[root.val] - 1 if noImpact else h - 1
            ans.append(memo[q])

        return ans
    
    def size(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def index(self, root: TreeNode, father: List[int], height: List[int], nodes: List[TreeNode]) -> int:
        heightLeft, heightRight = 0, 0
        nodes[root.val] = root
        if root.left is not None:
            father[root.left.val] = root.val
            heightLeft = self.index(root.left, father, height, nodes)
        if root.right is not None:
            father[root.right.val] = root.val
            heightRight = self.index(root.right, father, height, nodes)
        
        h = max(heightLeft + 1, heightRight + 1)
        height[root.val] = h
        return h


if __name__ == '__main__':
    print(Solution().treeQueries(TreeNode(1, TreeNode(3, TreeNode(2)),
          TreeNode(4, TreeNode(6), TreeNode(5, None, TreeNode(7)))), [4]))
    print(Solution().treeQueries(TreeNode(5, TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(
        6)), TreeNode(1)), TreeNode(9, TreeNode(3), TreeNode(7))), [3, 2, 4, 8]))

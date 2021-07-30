# LeetCode 987
# Vertical Order Traversal of a Binary Tree
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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        row_col_map = dict()
        self.traverse(root, 0, 0, row_col_map)
        row_col_arr = list(row_col_map.items())
        row_col_arr.sort(key = lambda x: x[0])
        ans = []
        for col, rows in row_col_arr:
            rows.sort()
            ans.append([x[1] for x in rows])
        return ans
        
    def traverse(self, root, row, col, row_col_map):
        if col not in row_col_map:
            row_col_map[col] = [(row, root.val)]
        else:
            row_col_map[col].append((row, root.val))
        if root.left is not None:
            self.traverse(root.left, row + 1, col - 1, row_col_map)
        if root.right is not None:
            self.traverse(root.right, row + 1, col + 1, row_col_map)

if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(5)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    print(Solution().verticalTraversal(nodes[0]))
    nodes = [TreeNode(i) for i in range(7)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    print(Solution().verticalTraversal(nodes[0]))

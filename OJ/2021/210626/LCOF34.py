# LeetCodeOffer 34 Medium
# Path Sum II
# Tree, Backtracing

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]: 
        ans = []
        if root is None:
            return ans
        path = [root.val]
        self.dfs(path, ans, root, 0, target)
        return ans

    def dfs(self, path: List[int], ans: List[List[int]], pos: TreeNode, cur_sum: int, target: int):
        cur_sum = cur_sum + pos.val
        
        # this pruning optimizition is not feasible, cuz val is not guaranteed to be positive
        # if cur_sum > target:
            # return 
        
        if pos.left is None and pos.right is None:
            if cur_sum == target:
                ans.append(list(path))
            return

        
        if pos.left is not None:
            path.append(pos.left.val)
            self.dfs(path, ans, pos.left, cur_sum, target)
            path.pop()

        if pos.right is not None:
            path.append(pos.right.val)
            self.dfs(path, ans, pos.right, cur_sum, target)
            path.pop()

if __name__ == "__main__":
    root = TreeNode(5, 
        TreeNode(4, 
            TreeNode(11, 
                TreeNode(7, None, None), 
                TreeNode(2, None, None)
            ),
            None), 
        TreeNode(8, 
            TreeNode(13, None, None), 
            TreeNode(4, 
                TreeNode(5, None, None), 
                TreeNode(1, None, None)
            )
        )
    )
    print(Solution().pathSum(root, 22))
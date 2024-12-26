# LeetCode 863
# All Nodes Distance K in Binary Tree
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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        if root == target:
            return self.getDownDistanceK(root, k, True, True)
        memo = dict() # in left sub tree = 1, in root sub tree = 2
        path = []
        self.find(root, target, path, memo)
        ans = []
        for i in range(len(path)):
            node = path[i]
            if memo[node] == 0: # target
                ans = ans + self.getDownDistanceK(node, k, True, True)
            elif memo[node] == 1: # target in left sub
                ans = ans + self.getDownDistanceK(node, k - i, False, True)
            elif memo[node] == 2:
                ans = ans + self.getDownDistanceK(node, k - i, True, False)
        return ans

    def find(self, root, target, path, memo):
        if root == target:
            path.append(target)
            memo[root] = 0
            return True
        if root is None:
            return False
        if self.find(root.left, target, path, memo):
            path.append(root)
            memo[root] = 1
            return True
        if self.find(root.right, target, path, memo):
            path.append(root)
            memo[root] = 2
            return True
        return False

        
    def getDownDistanceK(self, root, k, go_left, go_right):
        ans = []
        if root is None or k < 0:
            return ans
        if k == 0:
            ans.append(root.val)
            return ans
        if go_left:
            ans = ans + self.getDownDistanceK(root.left, k - 1, True, True)
        if go_right:
            ans = ans + self.getDownDistanceK(root.right, k - 1, True, True)
        return ans

if __name__ == "__main__":
    vals = [3, 5, 1, 6, 2, 0, 8, 7, 4]
    nodes = [TreeNode(val=vals[i]) for i in range(9)]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    nodes[4].left = nodes[7]
    nodes[4].right = nodes[8]
    # print(Solution().distanceK(nodes[0], nodes[1], 0))
    print(Solution().distanceK(nodes[0], nodes[1], 1))
    print(Solution().distanceK(nodes[0], nodes[1], 2))
    print(Solution().distanceK(nodes[0], nodes[1], 3))
    print(Solution().distanceK(nodes[7], nodes[7], 3))
    print(Solution().distanceK(nodes[0], nodes[0], 1))
    print(Solution().distanceK(nodes[0], nodes[0], 2))
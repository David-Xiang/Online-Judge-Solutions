# LeetCodeOffer 36 Medium
# Convert Binary Search Tree to Sorted Doubly Linked List
# Binary Search Tree

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None 
        left, right = self.dfs(root)
        left.left = right
        right.right = left
        return left

    def dfs(self, root):
        if root.left is None:
            left_start = root
        else:
            left_start, left_end = self.dfs(root.left)
            left_end.right = root
            root.left = left_end
        
        if root.right is None:
            right_end = root
        else:
            right_start, right_end = self.dfs(root.right)
            root.right = right_start
            right_start.left = root
        return (left_start, right_end)

        

if __name__ == "__main__":
    head = Node(4, 
        Node(2, 
            Node(1, None, None),
            Node(3, None, None)
        ),
        Node(5, None, None)
    )
    head = Solution().treeToDoublyList(head)
    print(head.val)
    pos = head.right
    while pos is not head:
        print(pos.val)
        pos = pos.right
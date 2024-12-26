# LeetCode 141
# Linked List Cycle
# Linked List

from typing import List
import collections
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pre = ListNode(0)
        pre.next = head
        slow, fast = pre, pre
        while slow != fast or slow == pre:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True

if __name__ == "__main__":
    nodes = [ListNode(i) for i in range(4)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[1]
    print(Solution().hasCycle(nodes[0]))
    nodes[1].next = nodes[0]
    print(Solution().hasCycle(nodes[0]))
    nodes[0].next = nodes[0]
    print(Solution().hasCycle(nodes[0]))
    nodes[0].next = None
    print(Solution().hasCycle(nodes[0]))
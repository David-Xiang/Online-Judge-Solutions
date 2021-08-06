# LeetCode 24
# Swap Nodes in Pairs
# Linked List

from typing import List
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre_head = ListNode(0, head)
        cur = pre_head
        while cur.next is not None and cur.next.next is not None:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return pre_head.next
        
if __name__ == "__main__":
    print(Solution().swapPairs(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))).val)
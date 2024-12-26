# LeetCode 19
# Remove Nth Node From End of List
# Linked List

from typing import List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for i in range(n):
            fast = fast.next
        pre_head = ListNode(0, head)
        slow_last = pre_head
        while fast is not None:
            fast = fast.next
            slow_last = slow_last.next
        slow_last.next = slow_last.next.next
        return pre_head.next

def test1():
    nodes = [ListNode(val=i) for i in range(5)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
    head = Solution().removeNthFromEnd(nodes[0], 2)
    while head is not None:
        print(head.val)
        head = head.next

def test2():
    nodes = [ListNode(val=i) for i in range(1)]
    head = Solution().removeNthFromEnd(nodes[0], 1)
    while head is not None:
        print(head.val)
        head = head.next

def test3():
    nodes = [ListNode(val=i) for i in range(2)]
    nodes[0].next = nodes[1]
    head = Solution().removeNthFromEnd(nodes[0], 1)
    while head is not None:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    test1()
    test2()
    test3()
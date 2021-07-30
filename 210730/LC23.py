# LeetCode 23
# Merge k Sorted Lists
# Heap/Priority Queue

from typing import List
import collections
import sys
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKListsNativeHeap(self, lists: List[ListNode]) -> ListNode:
        def __lt__(self, node): # class 排序需要重写lt方法
            return self.val < node.val
        ListNode.__lt__ = __lt__

        valid_count = 0
        valid_head = []
        for head in lists:
            if head is not None:
                valid_head.append(head)
                valid_count = valid_count + 1
        if valid_count == 0:
            return None
        elif valid_count == 1:
            return valid_head[0]
        
        q = []
        for head in valid_head:
            heapq.heappush(q, (head.val, head))
        ans_head = ListNode(0, None)
        ptr = ans_head
        while len(q) > 0:
            val, head = heapq.heappop(q)
            ptr.next = head
            ptr = ptr.next
            if head.next is not None:
                heapq.heappush(q, (head.next.val, head.next))
        return ans_head.next
    
    def mergeKLists(self, lists):
        valid_count = 0
        valid_head = []
        for head in lists:
            if head is not None:
                valid_head.append(head)
                valid_count = valid_count + 1
        if valid_count == 0:
            return None
        elif valid_count == 1:
            return valid_head[0]
        
        q = []
        for head in valid_head:
            self.my_heappush(q, head)
        ans_head = ListNode(0, None)
        ptr = ans_head
        while len(q) > 0:
            head = self.my_heappop(q)
            ptr.next = head
            ptr = ptr.next
            if head.next is not None:
                self.my_heappush(q, head.next)
        return ans_head.next

    def my_heappush(self, q, node):
        q.append(node)
        i = len(q) - 1
        while i != 0:
            father = (i - 1) // 2
            if q[father].val > q[i].val:
                q[i], q[father] = q[father], q[i]
                i = father
            else:
                break

    def my_heappop(self, q):
        top = q[0]
        last = q.pop()
        if len(q) == 0:
            return top
        q[0] = last
        i = 0
        while 2 * i + 2 < len(q):
            min_val = min(q[i].val, q[2 * i + 1].val, q[2 * i + 2].val)
            if min_val == q[2 * i + 1].val:
                q[i], q[2 * i + 1] = q[2 * i + 1], q[i]
                i = 2 * i + 1
            elif min_val == q[2 * i + 2].val:
                q[i], q[2 * i + 2] = q[2 * i + 2], q[i]
                i = 2 * i + 2
            else:
                break
        if 2 * i + 1 < len(q) and q[i].val > q[2 * i + 1].val:
            q[i], q[2 * i + 1] = q[2 * i + 1], q[i]
        return top

if __name__ == "__main__":
    head1 = ListNode(1, ListNode(4, ListNode(5, None)))
    head2 = ListNode(1, ListNode(3, ListNode(4, None)))
    head3 = ListNode(2, ListNode(6, None))
    head = Solution().mergeKLists([head1, head2, head3])
    while head is not None:
        print(head.val)
        head = head.next
    print(Solution().mergeKLists([]))
    print(Solution().mergeKLists([None]))

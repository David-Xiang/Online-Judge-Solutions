# LeetCode 1019
# Next Greater Node in Linked List
# Mononic Stack

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        arr = []
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        arr.reverse()
        
        stk = []
        ans = []
        for i in arr:
            while len(stk) > 0 and stk[-1] <= i:
                stk.pop()
            if len(stk) == 0:
                ans.append(0)
            else:
                ans.append(stk[-1])
            stk.append(i)
        ans.reverse()
        return ans

if __name__ == '__main__':
    head = ListNode(2, ListNode(1, ListNode(5, None)))
    head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5, None)))))
    head = ListNode(3, ListNode(3, None))
    print(Solution().nextLargerNodes(head))
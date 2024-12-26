# LeetCode 38
# Count and Say
# String

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        
        pre = ListNode(0, head)
        pos = pre
        while left > 1:
            pos = pos.next
            left = left - 1
            right = right - 1
        last = pos
        pos = pos.next
        import collections
        q = collections.deque()
        while right > 0:
            q.append(pos)
            pos = pos.next
            right = right - 1
        for i in range(len(q)):
            last.next = q.pop()
            last = last.next
        last.next = pos
        return pre.next

def printLinkedList(node):
    while node is not None:
        print(node.val)
        node = node.next

if __name__ == "__main__":
    node = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
    printLinkedList(Solution().reverseBetween(node, 2, 4))
    # node = ListNode(0)
    # printLinkedList(Solution().reverseBetween(node, 1, 1))    
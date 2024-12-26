# LeetCodeOffer 52
# Intersection of Two Linked Lists
# Two Pointers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next # not right: pa = pa.next if pa.next is not None else headB
            pb = headA if pb is None else pb.next
        return pa

def test1():
    nodes = [ListNode(i) for i in range(8)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[5].next = nodes[6]
    nodes[6].next = nodes[7]
    nodes[7].next = nodes[2]
    print(Solution().getIntersectionNode(nodes[0], nodes[5]).val)

def test2():
    nodes = [ListNode(i) for i in range(6)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[5].next = nodes[3]
    print(Solution().getIntersectionNode(nodes[0], nodes[5]).val)

def test3():
    nodes = [ListNode(i) for i in range(5)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[3].next = nodes[4]
    print(Solution().getIntersectionNode(nodes[0], nodes[3]).val)

if __name__ == "__main__":
    test1()
    test2()
    # test3()
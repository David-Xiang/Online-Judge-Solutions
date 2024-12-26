# LeetCodeOffer 35 Medium
# Copy List with Random Pointer
# Linked List

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList_not_good(self, head: 'Node') -> 'Node':
        # solution1: add all nodes to a map
        if head is None:
            return None
        copy_map = {}
        pos = head
        while pos is not None:
            copy_map[pos] = Node(pos.val, None, None)
            pos = pos.next
        for original_node, copy_node in copy_map.items():
            if original_node.next is not None:
                copy_node.next = copy_map[original_node.next]
            if original_node.random is not None:
                copy_node.random = copy_map[original_node.random]
        return copy_map[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        # solutionw: copy original random list in place(clone each node behind it)
        if head is None:
            return None
        pos = head
        while pos is not None: # clone in place
            clone = Node(pos.val, pos.next, None)
            pos.next = clone
            pos = pos.next.next
        pos = head
        while pos is not None: # rebuild random pointer
            clone = pos.next
            if pos.random is not None:
                clone.random = pos.random.next
            pos = pos.next.next
        pos = head
        copy_head = pos.next
        while pos is not None: # break one list into two
            clone = pos.next
            pos.next = pos.next.next
            if pos.next is not None:
                clone.next = pos.next.next
            else:
                clone.next = None
            pos = pos.next
        return copy_head

    def traverseRandomList(self, head: 'Node'):
        while head is not None:
            point_val = str(head.random.val) if head.random is not None else "null"
            print("Node (val = %d), random points to node(val = %s)" % (head.val, point_val))
            head = head.next

if __name__ == "__main__":
    solution = Solution()

    nodes1 = [
        Node(7, None, None),
        Node(13, None, None),
        Node(11, None, None),
        Node(10, None, None),
        Node(1, None, None),
    ]
    nodes1[0].next = nodes1[1]
    nodes1[1].next = nodes1[2]
    nodes1[2].next = nodes1[3]
    nodes1[3].next = nodes1[4]
    nodes1[1].random = nodes1[0]
    nodes1[2].random = nodes1[4]
    nodes1[3].random = nodes1[2]
    nodes1[4].random = nodes1[0]

    nodes2 = [
        Node(1, None, None),
        Node(2, None, None)
    ]
    nodes2[0].next = nodes2[1]
    nodes2[0].random = nodes2[1]
    nodes2[1].random = nodes2[1]

    nodes3 = [
        Node(1, None, None),
        Node(2, None, None),
        Node(3, None, None)
    ]
    nodes3[0].next = nodes3[1]
    nodes3[1].next = nodes3[2]
    nodes3[1].random = nodes3[0]

    # solution.traverseRandomList(nodes1[0])
    # solution.traverseRandomList(nodes2[0])
    # solution.traverseRandomList(nodes3[0])
    solution.traverseRandomList(solution.copyRandomList(nodes1[0]))
    solution.traverseRandomList(solution.copyRandomList(nodes2[0]))
    solution.traverseRandomList(solution.copyRandomList(nodes3[0]))

from __future__ import annotations
import random
from typing import List

INX_MAX = 1000000


class Node:
    def __init__(self, val: int, next: List[Node]):
        self.val = val
        self.next = next

    def print(self):
        print('val =', self.val, 'next =', [
              'None' if i is None else i.val for i in self.next])


class Skiplist:

    def __init__(self):
        self.size = 0
        self.head = Node(INX_MAX, [None])

    def print(self):
        print("Skiplist")
        print("size =", self.size)
        node = self.head
        while node is not None:
            node.print()
            node = node.next[0]

    def getTargetPrevNodesReversed(self, target: int) -> List[Node]:
        # level大的在前，0在最后
        prev: List[Node] = []
        node = self.head
        level = len(self.head.next) - 1
        while level >= 0:
            nextNode = node.next[level]
            if nextNode is not None and nextNode.val < target:
                node = nextNode
            else:
                prev.append(node)
                level = level - 1
        return prev

    def search(self, target: int) -> bool:
        if self.size == 0:
            return None

        prev = self.getTargetPrevNodesReversed(target)
        levelZeroNext = prev[-1].next[0]
        return levelZeroNext is not None and levelZeroNext.val == target

    def add(self, num: int) -> None:
        prev = self.getTargetPrevNodesReversed(num)

        self.size = self.size + 1
        height = len(self.head.next)
        node = Node(num, [])
        if self.size > 2 ** (height - 1):
            self.head.next.append(None)
        odd = 0.25
        for level in range(height):
            if level > 0 and random.random() > odd:
                break
            prevNode = prev.pop()
            node.next.append(prevNode.next[level])
            prevNode.next[level] = node

    def erase(self, num: int) -> bool:
        prev = self.getTargetPrevNodesReversed(num)

        suspect = prev[-1].next[0]
        if suspect is None or suspect.val != num:
            return False

        height = len(self.head.next)
        for level in range(height):
            node = prev.pop()
            if len(node.next) > level and node.next[level] is suspect:
                node.next[level] = suspect.next[level]
        self.size = self.size - 1
        return True


def test1():
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    skiplist.print
    print(skiplist.search(0))   # 返回 false
    skiplist.add(4)
    # skiplist.print()
    print(skiplist.search(1))   # 返回 true
    print(skiplist.erase(0))    # 返回 false，0 不在跳表中
    print(skiplist.erase(1))    # 返回 true
    print(skiplist.search(1))   # 返回 false，1 已被擦除


def test2():
    # ["Skiplist","add","add","add","add","search","erase","search","search","search"]
    # [[],[0],[5],[2],[1],[0],[5],[2],[3],[2]]
    skiplist = Skiplist()
    skiplist.add(0)
    skiplist.add(5)
    skiplist.add(2)
    skiplist.add(1)
    print(skiplist.search(0))   # 返回 true
    # skiplist.print()
    print(skiplist.erase(5))   # 返回 true
    print(skiplist.search(2))   # 返回 true
    print(skiplist.search(3))   # 返回 false
    print(skiplist.search(2))   # 返回 true


if __name__ == '__main__':
    test1()

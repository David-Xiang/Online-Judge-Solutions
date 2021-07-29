# LeetCode 146
# LRU Cache
# Linked List

from typing import List
import collections
import sys

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.last = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.next = self.head
        self.cap = capacity
        self.usage = 0
        self.map = dict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        if self.head.next != node:
            self.delink(node)
            self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.delink(node)
            self.insert(node)
            return
        
        if self.usage == self.cap:
            del self.map[self.tail.last.key]
            self.delink(self.tail.last)
            self.usage = self.usage - 1
            
        node = Node(key, value)
        self.insert(node)
        self.map[key] = node
        self.usage = self.usage + 1

    def delink(self, node):
        node.last.next = node.next
        node.next.last = node.last

    def insert(self, node):
        next_node = self.head.next
        self.head.next = node
        node.last = self.head
        node.next = next_node
        next_node.last = node
        

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
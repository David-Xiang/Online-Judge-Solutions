# LeetCode 225
# Implementing Stack Using Queues
# Number

from typing import List

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.qs = [collections.deque(), collections.deque()]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.qs[1].append(x)
        while len(self.qs[0]) > 0:
            self.qs[1].append(self.qs[0].popleft())
        self.qs[0], self.qs[1] = self.qs[1], self.qs[0]


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.qs[0].popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.qs[0][0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.qs[0]) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
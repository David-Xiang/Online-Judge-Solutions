# LeetCodeOffer 59-II
# Max Value in A Queue
# Monotonous Queue

from typing import List
import collections

class MaxQueue:

    def __init__(self):
        self.q = collections.deque()
        self.maxq = collections.deque()

    def max_value(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.maxq[0]

    def push_back(self, value: int) -> None:
        while len(self.maxq) > 0 and self.maxq[-1] < value:
            self.maxq.pop()
        self.maxq.append(value)
        self.q.append(value)


    def pop_front(self) -> int:
        if len(self.q) == 0:
            return -1
        if self.maxq[0] == self.q[0]:
            self.maxq.popleft()
        value = self.q.popleft()
        return value
        
def test1():
    q = MaxQueue()
    q.push_back(1)
    q.push_back(2)
    print(q.max_value())
    print(q.pop_front())
    print(q.max_value())

def test2():
    q = MaxQueue()
    print(q.pop_front())
    print(q.max_value())
        
if __name__ == "__main__":
    test1()
    test2()



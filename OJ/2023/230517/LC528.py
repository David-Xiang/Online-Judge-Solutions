
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.acc = 0
        for id in range(len(w)):
            self.acc = self.acc + w[id]
            self.prefix.append(self.acc)
    
    def pickIndex(self) -> int:
        rand = random.random() * self.acc
        left, right = 0, len(self.prefix)
        while left <= right:
            mid = left + (right - left) // 2
            if self.prefix[mid] > rand:
                right = mid - 1
            elif self.prefix[mid] < rand:
                left = mid + 1
            else:
                return mid
        return left

def test1():
    obj = Solution([1])
    print(obj.pickIndex())

def test2():
    obj = Solution([1, 3])
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())
    print(obj.pickIndex())

if __name__ == '__main__':
    test1()
    test2()

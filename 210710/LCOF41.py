# LeetCodeOffer 41
# Find Median from Data Stream
# Priority Queue
# large_half is small root heap
# small_half is large root heap and all of its elems are negative value
# large_half might store one more elem

from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large_half = []
        self.small_half = []

    def addNum(self, num: int) -> None:
        if len(self.large_half) == len(self.small_half):
            heapq.heappush(self.large_half, num)
        else:
            heapq.heappush(self.small_half, -num)

        if len(self.small_half) == 0:
            return
        
        if self.large_half[0] < - self.small_half[0]:
            large_root = heapq.heappushpop(self.large_half, -self.small_half[0])
            heapq.heappushpop(self.small_half, -large_root)

    def findMedian(self) -> float:
        if len(self.large_half) == 0:
            return 0
        if len(self.large_half) == len(self.small_half):
            return (self.large_half[0] - self.small_half[0]) / 2
        return self.large_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def test1():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())

def test2():
    obj = MedianFinder()
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())


if __name__ == "__main__":
    test1()
    test2()
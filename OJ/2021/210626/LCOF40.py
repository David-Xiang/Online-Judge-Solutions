# LeetCodeOffer 40
# Least K Numbers
# Sort

from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.qsort(arr, 0, len(arr), k)
        return sorted(arr[0:k])
    
    def qsort(self, arr, begin, end, num_item):
        if begin + 1 >= end:
            return

        pivot = arr[begin]
        pl = begin
        pr = end - 1
        while pl < pr:
            while pl < pr and arr[pr] > pivot:
                pr = pr - 1
            if pl < pr:
                arr[pl] = arr[pr]
                pl = pl + 1
            while pl < pr and arr[pl] < pivot:
                pl = pl + 1
            if pl < pr:
                arr[pr] = arr[pl]
                pr = pr - 1
        arr[pl] = pivot
        if pl - begin + 1 < num_item:
            self.qsort(arr, pl + 1, end, num_item - pl + begin - 1)
        elif pl - begin + 1 > num_item:
            self.qsort(arr, begin, pl, num_item)

if __name__ == "__main__":
    # print(Solution().getLeastNumbers([3,2,1], 2))
    # print(Solution().getLeastNumbers([0,1,2,1], 1))
    print(Solution().getLeastNumbers([0,1,1,1,4,5,3,7,7,8,10,2,7,8,0,5,2,16,12,1,19,15,5,18,2,2,22,15,8,22,17,6,22,6,22,26,32,8,10,11,2,26,9,12,9,7,28,33,20,7,2,17,44,3,52,27,2,23,19,56,56,58,36,31,1,19,19,6,65,49,27,63,29,1,69,47,56,61,40,43,10,71,60,66,42,44,10,12,83,69,73,2,65,93,92,47,35,39,13,75], 75))

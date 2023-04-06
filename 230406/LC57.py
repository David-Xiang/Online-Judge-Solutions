# LeetCode 57
# Insert Interval
# Simulation

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        toMerge = newInterval
        inserted = False

        ans = []
        for i in intervals:
            if self.isBefore(i, toMerge):
                ans.append(i)
            elif self.isBefore(toMerge, i):
                if not inserted:
                    ans.append(toMerge)
                ans.append(i)
                inserted = True
            else:
                toMerge = self.merge(i, toMerge)

        if not inserted:
            ans.append(toMerge)

        return ans

    def isBefore(self, a: List[int], b: List[int]):
        return a[1] < b[0]

    def merge(self, this: List[int], that: List[int]):
        return [min(this[0], that[0]), max(this[1], that[1])]


if __name__ == "__main__":
    print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(Solution().insert(intervals=[], newInterval=[5, 7]))
    print(Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]))
    print(Solution().insert(intervals=[[1, 5]], newInterval=[2, 7]))
    print(Solution().insert(intervals=[[2,5],[6,7],[8,9]], newInterval=[0, 1]))

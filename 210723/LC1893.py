# LeetCode 1893
# Check if All the Integers in a Range Are Covered
# Array

from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_in = []
        for r in ranges:
            x, y = r[0], r[1]
            if not y < left and not x > right: # 有交集
                ranges_in.append([max(x, left), min(y, right)])
        if len(ranges_in) == 0:
            return False
        ranges_in.sort(key=lambda r: r[0])
        print(ranges_in)
        pos = left - 1
        for r in ranges_in:
            if r[0] <= pos + 1:
                pos = max(r[1], pos)
        return pos >= right

if __name__ == "__main__":
    print(Solution().isCovered([[1,2],[3,4],[5,6]], 2, 5))
    print(Solution().isCovered([[1,10],[10,20]], 21, 21))
    print(Solution().isCovered([[13,43],[19,20],[32,38],[26,33],[3,38],[16,31],[26,48],[27,43],[12,24]], 36, 45))
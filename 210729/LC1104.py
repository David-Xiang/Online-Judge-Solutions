# LeetCode 1104
# Path In Zigzag Labelled Binary Tree
# Math

from typing import List
import collections
import sys

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        tmp, level = label, 0
        while tmp > 0:
            tmp = tmp // 2
            level = level + 1
        ans = [label]
        while ans[-1] != 1:
            if level % 2 == 0:
                ans.append((3 * 2 ** (level - 1) - ans[-1] - 1) // 2)
            else:
                ans.append(3 * 2 ** (level - 2) - ans[-1] // 2 - 1)
            level = level - 1
        return ans[::-1]

if __name__ == "__main__":
    print(Solution().pathInZigZagTree(14))
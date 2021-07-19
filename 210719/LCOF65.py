# LeetCodeOffer 65
# Add
# Bit Manipulation
# ~(a ^ mask): 32位以上的位取反，0至32位不变
from typing import List

class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xffffffff
        int_max = 0x7fffffff
        a, overflow = a & mask, b & mask
        while overflow != 0:
            a, overflow = (a ^ overflow), ((a & overflow) << 1) & mask
        return a if a <= int_max else ~(a ^ mask)

if __name__ == "__main__":
    print(Solution().add(1, 1))
    print(Solution().add(1, -1))
    print(Solution().add(-1, -1))
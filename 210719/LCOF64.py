# LeetCodeOffer 64
# Sum Sums
# Bit Manipulation

from typing import List

class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n - 1))

if __name__ == "__main__":
    print(Solution().sumNums(3))
    print(Solution().sumNums(9))
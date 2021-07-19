# LeetCodeOffer 62
# Last Remaining
# Math
# f(n, m)为n个人，剔除第m个人的最后一个人的编号
# 正序看老编号->新编号: old = (new + m) % n

from typing import List

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        return (self.lastRemaining(n - 1, m) + m) % n

if __name__ == "__main__":
    print(Solution().lastRemaining(5, 3))
    print(Solution().lastRemaining(10, 17))
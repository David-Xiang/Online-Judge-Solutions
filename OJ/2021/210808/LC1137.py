# LeetCode 1137
# N-th Tribonacci Number
# Array

from typing import List

class Solution:
    memo = [-1] * 40
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    def tribonacci(self, n: int) -> int:
        if self.memo[n] >= 0:
            return self.memo[n]
        self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.memo[n]
        

if __name__ == "__main__":
    print(Solution().tribonacci(0))
    print(Solution().tribonacci(1))
    print(Solution().tribonacci(4))
    print(Solution().tribonacci(25))
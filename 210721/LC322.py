# LeetCode 322
# Coin Change
# Dynamic Programming

from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < sys.maxsize else -1

if __name__ == "__main__":
    print(Solution().coinChange([1,2,5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([1], 0))
    print(Solution().coinChange([1], 1))
    print(Solution().coinChange([1], 2))
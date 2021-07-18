# LeetCodeOffer 60
# Dices Probability
# Dynamic Programming

from typing import List

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        maxs = n * 6
        dp = [[0 for i in range(maxs + 1)] for j in range(n + 1)]
        # dp[n][s] = prob of using n dices to get sum s
        for i in range(1, 7):
            dp[1][i] = 1 / 6
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for d in range(1, 7):
                    if j - d > 0:
                        dp[i][j] = dp[i][j] + dp[i - 1][j - d] / 6
        return dp[n][n:]

if __name__ == "__main__":
    print(Solution().dicesProbability(1))
    print(Solution().dicesProbability(2))
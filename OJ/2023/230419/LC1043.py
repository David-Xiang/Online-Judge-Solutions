from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            for j in range(1, k+1):
                if i - j == -1:
                    dp[i] = max(dp[i], j * max(arr[0: i + 1]))
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + j
                                * max(arr[i - j + 1: i + 1]))
        return dp[-1]


if __name__ == "__main__":
    print(Solution().maxSumAfterPartitioning(arr=[1, 15, 7, 9, 2, 5, 10], k=3))
    print(Solution().maxSumAfterPartitioning(
        arr=[1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], k=4))
    print(Solution().maxSumAfterPartitioning(arr=[1], k=1))

# LeetCode 300
# Longest Increasing Subsequence
# Dynamic Programming

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ans = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                ans = max(ans, dp[i])
        return ans

if __name__ == "__main__":
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(Solution().lengthOfLIS([0,1,0,3,2,3]))
    print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
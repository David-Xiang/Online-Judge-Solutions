# LeetCodeOffer 42
# Maximum Subarray
# Dynamic Programming

from typing import List

class Solution:
    def maxSubArraySlow(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            if dp[i-1] > 0:
                dp[i] += dp[i-1]
            if ans < dp[i]:
                ans = dp[i]
        return ans

    def maxSubArrayUnsafe(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if ans < nums[i]:
                ans = nums[i]
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        last_sum_max = nums[0]
        for i in range(1, len(nums)):
            this_sum_max = nums[i]
            if last_sum_max > 0:
                this_sum_max += last_sum_max
            if ans < this_sum_max:
                ans = this_sum_max
            last_sum_max = this_sum_max
        return ans

if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

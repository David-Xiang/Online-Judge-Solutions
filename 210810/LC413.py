# LeetCode 413
# Arithmetic Slices
# Dynamic Programming

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        last_count = 0
        ans = 0
        for i in range(2, len(nums)):
            if nums[i] + nums[i - 2] == nums[i - 1] + nums[i - 1]:
                last_count = last_count + 1
                ans = ans + last_count
            else:
                last_count = 0
        return ans

if __name__ == "__main__":
    print(Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))
    print(Solution().numberOfArithmeticSlices([1,2,3,4]))
    print(Solution().numberOfArithmeticSlices([1]))
# LeetCode 213
# House Robber II
# Dynamic Programming

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        rob0 = [0] * len(nums)
        rob1 = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                rob0[i] = nums[0]
                rob1[i] = 0
            elif i == 1:
                rob0[i] = nums[1]
                rob1[i] = nums[1]
            elif i == 2:
                rob0[i] = nums[0] + nums[2]
                rob1[i] = nums[2]
            else:
                rob0[i] = max(rob0[i-2], rob0[i-3]) + nums[i]
                rob1[i] = max(rob1[i-2], rob1[i-3]) + nums[i]
        return max(max(rob0[:-1]), max(rob1))

if __name__ == "__main__":
    print(Solution().rob([1]))
    print(Solution().rob([1, 2]))
    print(Solution().rob([2,3,2]))
    print(Solution().rob([1,2,3,1]))
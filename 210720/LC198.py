# LeetCode 198
# House Robber
# Dynamic Programming

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                rob[i] = nums[0]
            elif i == 1:
                rob[i] = nums[1]
            elif i == 2:
                rob[i] = nums[0] + nums[2]
            else:
                rob[i] = max(rob[i-2], rob[i-3]) + nums[i]
        return max(rob)

if __name__ == "__main__":
    print(Solution().rob([1,2,3,1]))
    print(Solution().rob([2,7,9,3,1]))
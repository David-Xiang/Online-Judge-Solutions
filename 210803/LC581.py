# LeetCode 581
# Shortest Unsorted Continuous Subarray
# Array

import pytest
from typing import List
import sys

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right_min = [nums[-1]] * len(nums)
        left_max = [nums[0]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])
        for i in range(1, len(nums)):
            left_max[i] = max(nums[i], left_max[i - 1])
        for lpos in range(len(nums)):
            if nums[lpos] > right_min[lpos]:
                lpos = lpos - 1
                break
            lpos = lpos + 1
        for rpos in range(len(nums) - 1, -1, -1):
            if nums[rpos] < left_max[rpos]:
                rpos = rpos + 1
                break
            rpos = rpos - 1
        return max(rpos - lpos - 1, 0)
    
if __name__ == "__main__":
    print(Solution().findUnsortedSubarray(([2,6,4,8,10,9,15])))
    print(Solution().findUnsortedSubarray([1,2,3,4]))
    print(Solution().findUnsortedSubarray([1]))
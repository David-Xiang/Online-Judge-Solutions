# LeetCode 15
# 3Sum
# Two Pointer

import pytest
from typing import List
import sys

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                k_minus, j_plus = False, False
                if s < 0:
                    j_plus = True
                elif s > 0:
                    k_minus = True
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j_plus = True
                    k_minus = True
                if j_plus:
                    j = j + 1
                    while nums[j] == nums[j - 1] and k > j:
                        j = j + 1
                if k_minus:
                    k = k - 1
                    while nums[k] == nums[k + 1] and k > j:
                        k = k - 1
        return ans
    
if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
    print(Solution().threeSum([]))
    print(Solution().threeSum([0]))
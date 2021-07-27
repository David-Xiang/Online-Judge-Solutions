# LeetCode 34
# Find First and Last Position of Element in Sorted Array
# Binary Search

from typing import List
import collections
import sys

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left_bound = self.searchLeft(nums, target)
        if left_bound == -1:
            return [-1, -1]
        return [left_bound, self.searchRight(nums, target)]

    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            left = -1
        return left

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0 or nums[right] != target:
            right = -1
        return right
    
if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))
    print(Solution().searchRange([5,7,7,8,8,10], 6))
    print(Solution().searchRange([], 8))
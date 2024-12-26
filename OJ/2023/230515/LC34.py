from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftBound(nums, target), self.rightBound(nums, target)]

    def leftBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1
            
        if left >= len(nums):
            return -1
        return left if nums[left] == target else -1
    
    def rightBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1
            
        if left < 1:
            return -1
        return left - 1 if nums[left - 1] == target else -1

if __name__ == '__main__':
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(Solution().searchRange(nums = [], target = 0))
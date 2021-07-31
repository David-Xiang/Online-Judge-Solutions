# LeetCode 26
# Remove Duplicates from Sorted Array
# Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        l, r, last = 1, 1, nums[0]
        while r < len(nums):
            if nums[r] > last:
                nums[l] = nums[r]
                l = l + 1
                last = nums[r]
            r = r + 1
        return l

if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2]))
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
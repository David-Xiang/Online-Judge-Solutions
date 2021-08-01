# LeetCode 283
# Move Zeros
# Array

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l = l + 1
            r = r + 1
        while l < len(nums):
            nums[l] = 0
            l = l + 1

if __name__ == "__main__":
    ans1 = [0,1,0,3,12]
    ans2 = [0]
    Solution().moveZeroes(ans1)
    Solution().moveZeroes(ans2)
    print(ans1)
    print(ans2)
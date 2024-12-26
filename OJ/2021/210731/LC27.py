# LeetCode 27
# Remove Element
# Array

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l = l + 1
            r = r + 1
        return l

if __name__ == "__main__":
    print(Solution().removeElement([3,2,2,3], 3))
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
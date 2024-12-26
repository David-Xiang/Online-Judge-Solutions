# LeetCode 912
# Sort an Array
# Sort

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums))
        return nums

    def sort(self, nums, begin, end):
        if begin >= end - 1:
            return
        pivot = nums[begin]
        p1, p2 = begin, end - 1
        while p1 < p2:
            while p1 < p2 and nums[p2] > pivot:
                p2 = p2 - 1
            if p1 < p2:
                nums[p1] = nums[p2]
                p1 = p1 + 1
            while p1 < p2 and nums[p1] < pivot:
                p1 = p1 + 1
            if p1 < p2:
                nums[p2] = nums[p1]
        nums[p1] = pivot
        self.sort(nums, begin, p1)
        self.sort(nums, p1 + 1, end)


if __name__ == "__main__":
    print(Solution().sortArray([5,2,3,1]))
    print(Solution().sortArray([5,1,1,2,0,0]))
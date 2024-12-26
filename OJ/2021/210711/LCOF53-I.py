# LeetCodeOffer 53-I
# Find First and Last Position of Element in Sorted Array
# Array

from typing import List

class Solution:
    # silly way, can do two binary: search(target) - search(target - 1)
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        pos = self.binarySearch(nums, target)
        if pos == -1:
            return 0
        pl, pr = pos, pos
        while pl - 1 >= 0 and nums[pl - 1] == nums[pos]:
            pl = pl - 1
        while pr + 1 < len(nums) and nums[pr + 1] == nums[pos]:
            pr = pr + 1
        return pr - pl + 1
                
    def binarySearch(self, nums, target):
        begin, end = 0, len(nums)
        while begin + 1 < end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                begin = mid
        if nums[begin] == target:
            return begin
        return -1
    
    def searchBetter(self, nums: List[int], target: int) -> int:
        def helper(target): # find the first position that larger than target
            begin, end = 0, len(nums) - 1
            while begin <= end: 
                mid = (begin + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1
            return begin
        return helper(target) - helper(target - 1)


if __name__ == "__main__":
    # print(Solution().search([5,7,7,8,8,10], 8))
    # print(Solution().search([5,7,7,8,8,10], 6))
    print(Solution().searchBetter([2, 2], 2))
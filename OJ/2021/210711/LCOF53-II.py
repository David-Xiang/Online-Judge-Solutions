# LeetCodeOffer 53-II
# Missing Number
# Binary Search

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == mid:
                begin = mid + 1
            else:
                end = mid - 1
        return begin

if __name__ == "__main__":
    print(Solution().missingNumber([0,1,3]))
    print(Solution().missingNumber([0,1,2,3,4,5,6,7,9]))
    print(Solution().missingNumber([1,2,3]))
    print(Solution().missingNumber([1]))
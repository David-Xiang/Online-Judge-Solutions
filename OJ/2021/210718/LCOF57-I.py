# LeetCodeOffer 57-I
# Two Sum
# Two Pointers

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        begin, end = 0, len(nums) - 1
        while begin < end:
            if nums[begin] + nums[end] < target:
                begin = begin + 1
            elif nums[begin] + nums[end] > target:
                end = end - 1
            else:
                return [nums[begin], nums[end]]
        return []

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([10,26,30,31,47,60], 40))
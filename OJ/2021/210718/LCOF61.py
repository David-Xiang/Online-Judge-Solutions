# LeetCodeOffer 61
# Straight
# Array

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
        n_zero = i
        zero_need = 0
        for i in range(n_zero, len(nums) - 1):
            if nums[i] == nums[i+1]:
                return False
            zero_need = zero_need + nums[i+1] - nums[i] - 1
        return zero_need <= n_zero

if __name__ == "__main__":
    print(Solution().isStraight([1,2,3,4,5]))
    print(Solution().isStraight([0,0,1,2,5]))
    print(Solution().isStraight([1,3,5,0,0]))
    print(Solution().isStraight([0,0,2,2,5]))
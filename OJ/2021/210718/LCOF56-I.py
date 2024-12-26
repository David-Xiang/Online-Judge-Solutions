# LeetCodeOffer 56-I
# Find Single Numbers in Array
# Bit Manipulation

from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor_val = 0
        for num in nums:
            xor_val = xor_val ^ num
        mask = 1
        # find the first bit that is not 0
        # get a mask to divide nums into 2 parts
        while mask & xor_val != mask:
            mask = mask << 1
        zero_val = 0
        one_val = 0
        for num in nums:
            if num & mask == mask:
                zero_val = zero_val ^ num
            else:
                one_val = one_val ^ num
        return [zero_val, one_val]

if __name__ == "__main__":
    print(Solution().singleNumbers([1,6]))
    print(Solution().singleNumbers([4,1,4,6]))
    print(Solution().singleNumbers([1,2,10,4,1,4,3,3]))
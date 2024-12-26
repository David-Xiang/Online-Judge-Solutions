# LeetCodeOffer 56-II
# Find Single Number in Array
# Bit Manipulation

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count every bit and mod 3
        ans = 0
        for index in range(32):
            count = 0
            for num in nums:
                if num >> index & 1 == 1:
                    count += 1
            if count % 3 == 1:
                ans += (1 << index)
        return ans

if __name__ == "__main__":
    print(Solution().singleNumber([3,4,3,3]))
    print(Solution().singleNumber([9,1,7,9,7,9,7]))
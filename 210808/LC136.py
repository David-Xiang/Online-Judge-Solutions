# LeetCode 136
# Single Number
# Array

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans

if __name__ == "__main__":
    print(Solution().singleNumber([2,2,1]))
    print(Solution().singleNumber([4,1,2,1,2]))
    print(Solution().singleNumber([1]))
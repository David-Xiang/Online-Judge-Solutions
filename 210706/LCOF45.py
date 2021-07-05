# LeetCodeOffer 45
# Smallest Number
# Array

from typing import List

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums_str = map(str, nums)
        # cmp_to_key func must return a number(pos: >, neg: <)
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        nums_str_sorted = sorted(nums_str, key = key)
        return "".join(nums_str_sorted)

if __name__ == "__main__":
    print(Solution().minNumber([10,2]))
    print(Solution().minNumber([3,30,34,5,9]))

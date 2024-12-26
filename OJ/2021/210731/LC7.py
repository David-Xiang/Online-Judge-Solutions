# LeetCode 7
# Reverse Integer
# Number

from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        pos = True if x > 0 else False
        x = x if x > 0 else -x
        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10
        ans = 0
        for num in nums:
            ans = ans * 10 + num
        if not pos:
            ans = -ans
        if ans >= 1 << 31 or ans < - 1 << 31:
            ans = 0
        return ans
            

if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
# LeetCodeOffer 43
# Number Of Digit One
# Math

from typing import List

class Solution:
    def countDigitOne(self, n: int) -> int:
        high, low, curr, ans = 0, 0, 0, 0
        digit = 1
        while n != 0:
            curr = n % 10
            high = n // 10
            if curr == 0:
                ans += high * digit
            elif curr == 1:
                ans += high * digit + low + 1
            else:
                ans += (high + 1) * digit
            low += curr * digit
            digit *= 10
            n //= 10
        return ans

if __name__ == "__main__":
    print(Solution().countDigitOne(1))
    print(Solution().countDigitOne(12))
    print(Solution().countDigitOne(13))
# LeetCodeOffer 44
# Nth Digit
# Math

from typing import List

class Solution:
    def findNthDigit(self, n: int) -> int:
        length_of_digits = self.getLengthsOfNDigits()
        length = 1
        # calculate current length
        while length_of_digits[length] <= n:
            length += 1

        # calculate real number and the offset in this number
        res_len = n - length_of_digits[length]
        real_num = res_len // length + pow(10, length)
        real_offset = n - length_of_digits[length] - (real_num - pow(10, length)) * length
        return self.getOffsetFromN(real_num, real_offset)
        
    def getOffsetFromN(self, n, offset):
        if n == 0:
            return 0
        arr = []
        while n != 0: 
            arr.append(n % 10)
            n //= 10
        reverse_arr = arr[::-1]
        return reverse_arr[offset]

    def getLengthsOfNDigits(self):
        ans = [0, 10]
        for i in range(2, 20):
            length = (pow(10, i) - pow(10, i-1)) * i
            ans.append(length + ans[-1])
        return ans

if __name__ == "__main__":
    print(Solution().findNthDigit(0))
    print(Solution().findNthDigit(3))
    print(Solution().findNthDigit(9))
    print(Solution().findNthDigit(10))
    print(Solution().findNthDigit(11))
    print(Solution().findNthDigit(12))
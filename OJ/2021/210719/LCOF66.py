# LeetCodeOffer 66
# Construct Array
# Array

from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        ans = [1] * len(a)
        for i in range(1, len(a)):
            ans[i] = ans[i - 1] * a[i - 1]
        mul = 1
        for i in range(len(a) - 2, -1, -1):
            mul = mul * a[i + 1]
            ans[i] = ans[i] * mul
        return ans

if __name__ == "__main__":
    print(Solution().constructArr([1,2,3,4,5]))
    print(Solution().constructArr([2,3]))
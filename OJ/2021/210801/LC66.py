# LeetCode 66
# Plus One
# Array

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = list(digits)
        for i in range(len(digits)-1, -1, -1):
            ans[i] = ans[i] + carry
            carry = 0
            if ans[i] > 9:
                ans[i] = ans[i] - 10
                carry = 1
        if carry == 1:
            ans = [1] + ans
        return ans

        

if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))
    print(Solution().plusOne([4,3,2,1]))
    print(Solution().plusOne([0]))
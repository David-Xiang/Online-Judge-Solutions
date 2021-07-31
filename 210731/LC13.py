# LeetCode 13
# Roman to Integer
# Number

from typing import List

class Solution:
    cToInt = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            val = self.cToInt[s[i]]
            if s[i:i+2] in ("IV", "IX", "XL", "XC", "CD", "CM"):
                val = -val
            ans = ans + val
        ans = ans + self.cToInt[s[len(s)-1]]
        return ans
        

if __name__ == "__main__":
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
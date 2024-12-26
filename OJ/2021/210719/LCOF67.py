# LeetCodeOffer 67
# String to Integer
# String

from typing import List

class Solution:
    digit_map = {"1": 1, "2": 2, "3": 3, "4":4, "5":5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    int_max = 2147483647
    int_min = -2147483648

    def strToInt(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        i = 0
        positive = True
        if s[i] not in "+-1234567890":
            return 0
        elif s[i] == "+":
            i = i + 1
        elif s[i] == "-":
            positive = False
            i = i + 1
        ans = 0
        for i in range(i, len(s)):
            if s[i] not in "1234567890":
                break
            ans = ans * 10 + self.digit_map[s[i]]
            i = i + 1
        if positive:
            return ans if ans <= self.int_max else self.int_max
        return -ans if -ans >= self.int_min else self.int_min

if __name__ == "__main__":
    print(Solution().strToInt("42"))
    print(Solution().strToInt("   -42"))
    print(Solution().strToInt("4193 with words"))
    print(Solution().strToInt("words and 987"))
    print(Solution().strToInt("-91283472332"))
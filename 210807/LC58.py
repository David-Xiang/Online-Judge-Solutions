# LeetCode 58
# Length of Last Word
# String

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_counted = False
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if letter_counted:
                    break
            else:
                letter_counted = True
                ans = ans + 1
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
    print(Solution().lengthOfLastWord("     "))
# LeetCode 9
# Palindrome Number
# Number

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
            

if __name__ == "__main__":
    print(Solution().isPalindrome(123))
    print(Solution().isPalindrome(-123))
    print(Solution().isPalindrome(120))
    print(Solution().isPalindrome(0))
# LeetCodeOffer 58-II
# Reverse Left Words in a String
# String

from typing import List

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]
        
if __name__ == "__main__":
    print(Solution().reverseLeftWords("abcdefg", 2))
    print(Solution().reverseLeftWords("lrloseumgh", 6))
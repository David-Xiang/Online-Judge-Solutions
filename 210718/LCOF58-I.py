# LeetCodeOffer 58-I
# Reverse Words in a String
# String, Two Pointers

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        # words = [w for w in s.strip().split(" ") if len(w.strip()) > 0]
        words.reverse()
        return " ".join(words)
    
    def reverseWordsTwoPointer(self, s: str) -> str:
        words = []
        i, j = 0, 0
        find = True
        while i < len(s):
            if j == len(s):
                words.append(s[i:j])
                i = j
            elif s[j] != ' ':
                find = False
                j = j + 1
            elif find:
                j = j + 1
                i = j
            else:
                words.append(s[i:j])
                find = True
        words.reverse()
        return " ".join(words)


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world!  "))
    print(Solution().reverseWords("a good   example"))
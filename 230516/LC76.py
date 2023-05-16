from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        chars = set(t)
        left, right = 0, 0
        ans = ''
        while right < len(s):
            if s[right] in chars:
                needed.subtract(s[right])

            right = right + 1

            valid = True
            for c in chars:
                if needed[c] > 0:
                    valid = False

            while valid and left < right:
                if right - left < len(ans) or len(ans) == 0:
                    ans = s[left: right]
                
                if s[left] in chars:
                    needed.update(s[left])
                    if needed[s[left]] > 0:
                        valid = False
                
                left = left + 1
        
        return ans

if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
    print(Solution().minWindow(s="a", t="a"))
    print(Solution().minWindow(s="a", t="aa"))

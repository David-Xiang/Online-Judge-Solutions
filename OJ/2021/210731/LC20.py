# LeetCode 20
# Valid Parentheses
# Stack

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        import collections
        stk = collections.deque()
        for c in s:
            if c in "({[":
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                top = stk.pop()
                if top + c not in ["()", "[]", "{}"]:
                    return False
        return len(stk) == 0

if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
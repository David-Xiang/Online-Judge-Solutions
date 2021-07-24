# LeetCode 1736
# Latest Time by Replacing Hidden Digits
# String

from typing import List

class Solution:
    def maximumTime(self, time: str) -> str:
        ans = list(time)
        if ans[0] == '?':
            ans[0] = '2' if ans[1] not in "456789" else "1"
        if ans[1] == '?':
            ans[1] = '3' if ans[0] == '2' else '9'
        if ans[3] == '?':
            ans[3] = '5'
        if ans[4] == '?':
            ans[4] = '9'
        return ''.join(ans)

if __name__ == "__main__":
    print(Solution().maximumTime("2?:?0"))
    print(Solution().maximumTime("0?:3?"))
    print(Solution().maximumTime("??:3?"))
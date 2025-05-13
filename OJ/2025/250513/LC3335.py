#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res = 0
        lookup = "abcdefghijklmnopqrstuvwxyz"
        for c in s:
            res = (res + self.f(lookup.index(c), t)) % 1000000007
        return res

    def f(self, c, t):
        if (c, t) in self.memo:
            return self.memo[(c, t)]
        elif t + c < 26:
            res = 1
        else:
            res = (self.f(0, t + c - 26) + self.f(1, t + c - 26)) % 1000000007
        self.memo[(c, t)] = res
        return res


# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517))

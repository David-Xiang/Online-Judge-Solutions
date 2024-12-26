from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        dp = {i: 1 for i in words}
        ans = 1
        for w in words:
            if len(w) == 1:
                continue
            for l in range(len(w)):
                nw = w[:l] + w[l+1:]
                if nw in dp:
                    dp[w] = max(dp[w], dp[nw] + 1)
                    ans = max(ans, dp[w])
        return ans


if __name__ == '__main__':
    print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
    print(Solution().longestStrChain(["abcd", "dbqca"]))

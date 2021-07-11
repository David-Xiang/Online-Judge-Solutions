# LeetCodeOffer 46
# Ways of Translations
# Dynamic Programming

class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        chars = []
        while num != 0:
            chars.append(num % 10)
            num //= 10
        chars = chars[::-1]
        dp = [0] * (len(chars) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(chars) + 1):
            dp[i] = dp[i - 1]
            val = chars[i-2] * 10 + chars[i-1]
            if val >= 10 and val < 26:
                dp[i] += dp[i - 2]
        return dp[len(chars)]
        

if __name__ == "__main__":
    print(Solution().translateNum(12258))
    print(Solution().translateNum(505))
    print(Solution().translateNum(0))
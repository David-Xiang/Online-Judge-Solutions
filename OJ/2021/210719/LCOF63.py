# LeetCodeOffer 63
# Best Time to Buy and Sell Stock
# Dynamic Programming

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minp, ans = prices[0], 0
        for i in prices:
            minp = min(minp, i)
            ans = max(ans, i - minp)
        return ans

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([7,6,4,3,1]))
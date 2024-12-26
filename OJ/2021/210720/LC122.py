# LeetCode 122
# Best Time to Buy and Sell Stock II
# Dynamic Programming

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_buy, max_sell = - prices[0], 0
        for i in range(1, len(prices)):
            max_buy, max_sell = max(max_buy, max_sell - prices[i]), max(max_sell, prices[i] + max_buy)
        return max_sell

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([1,2,3,4,5]))
    print(Solution().maxProfit([7,6,4,3,1]))
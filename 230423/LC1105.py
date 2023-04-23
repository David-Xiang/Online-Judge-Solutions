from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        INT_MAX = 10000000
        dp = [INT_MAX] * len(books)
        dp[0] = books[0][1]
        for i in range(1, len(books)):
            w, h = books[i]
            dp[i] = dp[i - 1] + h
            for j in range(i - 1, -1, -1):
                w = w + books[j][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j][1])
                dp[i] = min(dp[i], dp[j - 1] + h if j > 0 else h)
        return dp[len(books) - 1]
            

if __name__ == "__main__":
    print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
    print(Solution().minHeightShelves([[1,3],[2,4],[3,2]], 6))
    print(Solution().minHeightShelves([[7,3],[8,7],[2,7],[2,5]], 10))
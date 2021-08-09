# LeetCode 313
# Super Ugly Number
# Math

from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        q = []
        s = set()
        q.append(1)
        s.add(1)
        for i in range(n):
            ans = heapq.heappop(q)
            for prime in primes:
                adj = ans * prime
                if adj not in s:
                    heapq.heappush(q, adj)
                    s.add(adj)
        return ans

if __name__ == "__main__":
    print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))
    print(Solution().nthSuperUglyNumber(1, [2,3,5]))
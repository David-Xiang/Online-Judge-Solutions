# LeetCode 739
# Daily Temperatures
# Monotonic Stack

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        import collections
        stk = collections.deque()
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stk) > 0 and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if len(stk) == 0:
                ans.append(0)
            else:
                ans.append(stk[-1] - i)
            stk.append(i)
        return ans[::-1]

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(Solution().dailyTemperatures([30,40,50,60]))
    print(Solution().dailyTemperatures([30,60,90]))
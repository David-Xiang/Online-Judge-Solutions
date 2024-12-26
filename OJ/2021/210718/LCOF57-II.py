# LeetCodeOffer 57-II
# Find Continuous Sequence
# Two Pointers, Sliding Window

from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        begin, end = 1, 2
        s = begin + end
        ans = []
        while begin < end:
            if s < target:
                end = end + 1
                s = s + end
            else:
                if s == target:
                    ans.append([i for i in range(begin, end + 1)])
                s = s - begin
                begin = begin + 1
        return ans

if __name__ == "__main__":
    print(Solution().findContinuousSequence(1))
    print(Solution().findContinuousSequence(2))
    print(Solution().findContinuousSequence(3))
    print(Solution().findContinuousSequence(9))
    print(Solution().findContinuousSequence(15))
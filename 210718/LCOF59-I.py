# LeetCodeOffer 59-I
# Sliding Window Maximum
# Sliding Window, Monotonous Queue

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue append index
        q = collections.deque()
        ans = []
        for i in range(len(nums)):
            while len(q) > 0 and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
        
        
if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(Solution().maxSlidingWindow([1], 1))
    print(Solution().maxSlidingWindow([1,-1], 1))
    print(Solution().maxSlidingWindow([9,11], 2))
    print(Solution().maxSlidingWindow([4,-2], 2))
    print(Solution().maxSlidingWindow([], 2))



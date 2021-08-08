# LeetCode 918
# Maximum Sum Circular Subarray
# Dynamic Programming/Monotonic Queue
# DP：环形的最大值两种情况：1中间的连续区间最大，2涉及首尾拼接的区间最大，考虑反面：中间的连续区间必然最小
# MQ：将环展成两个拼接的数组，然后求滑动窗口的最值

from typing import List

class Solution:
    def maxSubarraySumCircularMonotonicQueue(self, nums: List[int]) -> int:
        arr = nums + nums
        k = len(nums)
        prefix = [0] * len(arr)
        last = 0
        for i in range(len(arr)):
            last = arr[i] + last
            prefix[i] = last
        import sys
        ans = -sys.maxsize
        import collections
        q = collections.deque()
        q.append((-1, 0))
        for j in range(len(arr)):
            if q[0][0] < j - k:
                q.popleft()
            ans = max(ans, prefix[j] - q[0][1])
            while len(q) > 0 and q[-1][1] >= prefix[j]:
                q.pop()
            q.append((j, prefix[j]))
        return ans

    def maxSubarraySumCircular(self, nums: List[int]) -> int: # dp做法
        import sys
        ans_max = -sys.maxsize
        ans_min = sys.maxsize
        last_max, last_min = 0, 0
        sum_arr = 0
        for i in nums:
            sum_arr = sum_arr + i
            last_max = i if last_max <= 0 else last_max + i
            last_min = i if last_min > 0 else last_min + i
            ans_max = max(ans_max, last_max)
            ans_min = min(ans_min, last_min)
        if ans_min == sum_arr:
            return ans_max
        return max(ans_max, sum_arr - ans_min)

if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([1,-2,3,-2]))
    print(Solution().maxSubarraySumCircular([5,-3,5]))
    print(Solution().maxSubarraySumCircular([3,-1,2,-1]))
    print(Solution().maxSubarraySumCircular([3,-2,2,-3]))
    print(Solution().maxSubarraySumCircular([-2,-3,-1]))
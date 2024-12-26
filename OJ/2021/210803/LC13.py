# LeetCode 13
# Container With Most Water
# Two Pointer
# 这里的双指针可以看作是在对n^2的解空间进行剪枝，
# 因为单移动长边造成的解一定只会变小
# 因此我们先移动短边

import pytest
from typing import List
import sys

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[r] < height[l]:
                r = r - 1
            else:
                l = l + 1
        return ans
    
if __name__ == "__main__":
    print(Solution().maxArea(([1,8,6,2,5,4,8,3,7])))
    print(Solution().maxArea([1,1]))
    print(Solution().maxArea([4,3,2,1,4]))
    print(Solution().maxArea([1,2,1]))
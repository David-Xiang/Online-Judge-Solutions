# LeetCode 1838
# Frequency of the Most Frequent Element
# Two Pointers
# 经典的双指针用法，左指针右移 -> sum减少，右指针移动 -> sum增加
# 需要注意sum减少的算法和增加的算法是不一样的

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        i, j, s, ans = 0, 1, 0, 1
        while j < len(nums):
            s = s + (j - i) * (nums[j] - nums[j - 1])
            while i < j and s > k:
                s = s - (nums[j] - nums[i])
                i = i + 1
            ans = max(ans, j - i + 1)
            j = j + 1
        return ans

if __name__ == "__main__":
    print(Solution().maxFrequency([1,2,4], 5))
    print(Solution().maxFrequency([1,4,8,13], 5))
    print(Solution().maxFrequency([3,9,6], 2))
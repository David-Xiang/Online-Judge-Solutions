#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#

from typing import List

# @lc code=start


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ans = 1
        pre_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
        i, j = 0, 0
        while j < len(nums):
            while i < j:
                pre_sum_im1 = pre_sum[i - 1] if i > 0 else 0
                if (j - i + 1) * nums[j] - pre_sum[j] + pre_sum_im1 <= k:
                    # find a solution
                    break
                i = i + 1
            ans = max(ans, j - i + 1)
            j = j + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    f = Solution().maxFrequency
    assert f([1, 2, 4], k=5) == 3
    assert f([1, 4, 8, 13], k=5) == 2
    assert f([3, 9, 6], k=2) == 1

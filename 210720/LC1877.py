# LeetCode 1877
# Minimize Maximum Pair Sum in Array
# Array

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        length = len(nums)
        for i in range(0, length):
            ans = max(ans, nums[i] + nums[length - i - 1])
        return ans

if __name__ == "__main__":
    print(Solution().minPairSum([3,5,2,3]))
    print(Solution().minPairSum([3,5,4,2,4,6]))
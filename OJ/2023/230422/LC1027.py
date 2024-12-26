from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [dict() for i in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                length = dp[j].get(diff, 1) + 1
                ans = max(ans, length)
                dp[i][diff] = length
        return ans

if __name__ == '__main__':
    print(Solution().longestArithSeqLength([3,6,9,12]))
    print(Solution().longestArithSeqLength([9,4,7,2,10]))
    print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))
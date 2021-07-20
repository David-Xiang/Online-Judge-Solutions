# LeetCode 55
# Jump Game
# Dynamic Programming

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i in range(len(nums)):
            if i > max_pos:
                return False
            max_pos = max(max_pos, i + nums[i])
        return True

if __name__ == "__main__":
    print(Solution().canJump([2,3,1,1,4]))
    print(Solution().canJump([3,2,1,0,4]))
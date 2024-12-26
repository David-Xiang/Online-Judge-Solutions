# LeetCode 45
# Jump Game II
# Dynamic Programming

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_pos, next_max_pos = nums[0], nums[0]
        step = 1
        for i in range(1, len(nums)):
            if i > max_pos:
                step = step + 1
                max_pos = next_max_pos
            next_max_pos = max(next_max_pos, i + nums[i])
        return step
    
    

if __name__ == "__main__":
    print(Solution().jump([2,3,1,1,4]))
    print(Solution().jump([2,3,0,1,4]))
    print(Solution().jump([1,2,3]))
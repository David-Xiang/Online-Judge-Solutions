# LeetCode 457
# Circular Array Loop
# Array

from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for pos in range(len(nums)):
            delta = nums[pos]
            this_round = 1000 + pos + 1
            if delta > 1000 or delta < -1000:
                continue
            nums[pos] = this_round
            next_pos = (pos + delta) % len(nums)
            if delta % len(nums) == 0:
                continue
            while nums[next_pos] <= 1000 and nums[next_pos] >= -1000 and nums[next_pos] * delta > 0:
                next_delta = nums[next_pos]
                nums[next_pos] = this_round
                if next_delta % len(nums) == 0:
                    break
                next_pos = (next_pos + next_delta) % len(nums)
                if nums[next_pos] == this_round:
                    return True
        return False


if __name__ == "__main__":
    print(Solution().circularArrayLoop([2,-1,1,2,2]))
    print(Solution().circularArrayLoop([-1,2]))
    print(Solution().circularArrayLoop([-2,1,-1,-2,-2]))
    print(Solution().circularArrayLoop([3,1,2]))
    print(Solution().circularArrayLoop([-1,-2,-3,-4,-5]))
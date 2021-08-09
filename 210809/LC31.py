# LeetCode 31
# Next Permutation
# Array

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        for first_pos in range(len(nums) - 2, -1, -1):
            if nums[first_pos] < nums[first_pos + 1]:
                break
        if first_pos == 0 and nums[0] >= nums[1]:
            nums.sort()
            return
        candidate = nums[first_pos:]
        candidate.sort()
        for i in range(len(nums) - 1):
            if candidate[i] == nums[first_pos] and candidate[i + 1] != nums[first_pos]:
                break
        remains = candidate[:i+1] + candidate[i+2:]
        remains.sort()
        nums[first_pos] = candidate[i + 1]
        for i in range(first_pos + 1, len(nums)):
            nums[i] = remains[i - first_pos - 1]
        print(nums)

if __name__ == "__main__":
    # Solution().nextPermutation([1,2,3])
    # Solution().nextPermutation([3,2,1])
    # Solution().nextPermutation([1,1,5])
    # Solution().nextPermutation([1])
    # Solution().nextPermutation([1,4,3,2])
    Solution().nextPermutation([1,5,1])
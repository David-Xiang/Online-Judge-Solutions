# LeetCode 287
# Find the Duplicate Number
# Array

from typing import List
import collections
import sys

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] - 1 == i:
                continue
            pos = nums[i] - 1
            while pos != i:
                if pos < i:
                    return pos + 1
                tmp = nums[pos]
                if tmp == pos + 1:
                    return tmp
                nums[pos] = pos + 1
                pos = tmp - 1

            

if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))
    print(Solution().findDuplicate([1,1]))
    print(Solution().findDuplicate([1,1,2]))
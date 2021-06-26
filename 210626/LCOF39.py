# LeetCodeOffer 39 Easy
# Majority Element
# Array

from typing import List

class Solution:
    def majorityElement_slow(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if len(stack) == 0 or stack[0] == i:
                stack.append(i)
            else:
                stack.pop()
        return stack[0]
    
    def majorityElement(self, nums: List[int]) -> int:
        stack_item = 0
        stack_count = 0
        for i in nums:
            if stack_count == 0 or stack_item == i:
                stack_count = stack_count + 1
                stack_item = i
            else:
                stack_count = stack_count - 1
        return stack_item

if __name__ == "__main__":
    print(Solution().majorityElement([1]))
    print(Solution().majorityElement([1, 2, 1]))
    print(Solution().majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
# LeetCode 169
# Major Element
# Array

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        stk = collections.deque()
        for i in nums:
            if len(stk) > 0 and stk[-1] != i:
                stk.pop()
            else:
                stk.append(i)
        return stk[-1]
    
if __name__ == "__main__":
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
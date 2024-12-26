# LeetCode 78
# Subsets
# DFS

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = 2 ** len(nums)
        ans = []
        for i in range(length):
            subset = []
            tmp = i
            cnt = 0
            while tmp > 0:
                if tmp & 1 == 1:
                    subset.append(nums[cnt])
                tmp = tmp >> 1
                cnt = cnt + 1
            
            ans.append(subset)
        
        return ans
        

if __name__ == '__main__':
    print(Solution().subsets([1,2,3,4,5,6,7,8,9,0]))
    print(Solution().subsets([1]))
# LeetCode 2404
# Most Frequent Even Element
# Array

from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n % 2 == 1:
                continue
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1
        ans = -1
        d[ans] = 0

        for (n, count) in d.items():
            if count > d[ans] or (count == d[ans] and n < ans):
                ans = n     
        return ans
    
if __name__ == "__main__":
    print(Solution().mostFrequentEven([0,1,2,2,4,4,1]))
    print(Solution().mostFrequentEven([4,4,4,9,2,4]))
    print(Solution().mostFrequentEven([29,47,21,41,13,37,25,7]))
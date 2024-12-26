# LeetCodeOffer 51
# Reverse Pairs
# Sort

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tmp = [0] * len(nums)
        return self.mergeSort(nums, tmp, 0, len(nums))

    def mergeSort(self, arr, tmp, begin, end):
        if begin + 1 >= end:
            return 0
        mid = (begin + end) // 2
        count = self.mergeSort(arr, tmp, begin, mid) + self.mergeSort(arr, tmp, mid, end)
        i, j, p = begin, mid, begin
        while i < mid and j < end:
            while i < mid and arr[i] <= arr[j]:
                tmp[p] = arr[i]
                p += 1
                i += 1
                count += j - mid
            # if i >= mid:
            #     break
            while j < end and arr[i] > arr[j]:
                tmp[p] = arr[j]
                p += 1
                j += 1
        while i < mid:
            tmp[p] = arr[i]
            p += 1
            i += 1
            count += j - mid
        while j < end:
            tmp[p] = arr[j]
            p += 1
            j += 1
        arr[begin:end] = tmp[begin:end]
        return count

if __name__ == "__main__":
    print(Solution().reversePairs([7,5,6,4]))
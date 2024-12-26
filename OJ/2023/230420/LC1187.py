
from typing import List

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        INT_MAX = 10000000
        if len(arr1) == 1:
            return 0
        arr2 = list(set(arr2))
        arr2.sort()
        change = [[INT_MAX for i in range(len(arr2))] for j in range(len(arr1))]
        for i in range(len(arr2)):
            change[0][i] = 1
        nochange = [INT_MAX for i in range(len(arr1))]
        nochange[0] = 0
        for i in range(1, len(arr1)):
            if arr1[i] > arr1[i - 1]:
                nochange[i] = min(nochange[i], nochange[i-1])
            for j in range(len(arr2)):
                if arr1[i] > arr2[j]:
                    nochange[i] = min(nochange[i], change[i-1][j])
            
            for j in range(len(arr2)):
                if arr2[j] > arr1[i-1]:
                    change[i][j] = min(change[i][j], nochange[i-1])
                for k in range(j-1, -1, -1):
                    if arr2[j] > arr2[k]:
                        change[i][j] = min(change[i][j], change[i-1][k])
                        break
                change[i][j] = change[i][j] + 1
        ans = min(nochange[-1], min(change[-1]))
        return ans if ans < INT_MAX else -1



if __name__ == "__main__":
    print(Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]))
    print(Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1]))
    print(Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]))
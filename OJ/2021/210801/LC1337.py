# LeetCode 1337
# The K Weakest Rows in a Matrix
# Array

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    break
                count = count + 1
            arr.append((count, i))
        arr.sort()
        print(arr)
        return [arr[i][1] for i in range(k)]
        

if __name__ == "__main__":
    print(Solution().kWeakestRows([[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]], 
        3))
    print(Solution().kWeakestRows([[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]], 
        2))
    print(Solution().kWeakestRows([[1,1,1,1,1],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,0],[1,1,1,1,1]], 3))
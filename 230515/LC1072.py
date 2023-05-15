from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()
        for row in matrix:
            ans = 0
            for i in row:
                ans = ans * 10 + i ^ row[0]
            counter.update([ans])
        return max(counter.values())

if __name__ == '__main__':
    print(Solution().maxEqualRowsAfterFlips([[0,1],[1,1]]))
    print(Solution().maxEqualRowsAfterFlips([[0,1],[1,0]]))
    print(Solution().maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
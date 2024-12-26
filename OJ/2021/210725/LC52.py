# LeetCode 52
# N-Queens II
# Backtracking

from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        self.backtrace(n, 0, [], ans)
        return len(ans)

    def backtrace(self, n, now_row, used, ans):
        if now_row == n:
            ans.append(1)
            return
        
        for now_col in range(n):
            if self.isValid(now_row, now_col, used):
                used.append(now_col)
                self.backtrace(n, now_row + 1, used, ans)
                used.pop()
                
    def isValid(self, now_row, now_col, used):
        for row in range(len(used)):
            col = used[row]
            if now_col == col:
                return False
            if now_col - col == now_row - row:
                return False
            if now_col + now_row == col + row:
                return False
        return True

if __name__ == "__main__":
    print(Solution().totalNQueens(1))
    print(Solution().totalNQueens(4))
    print(Solution().totalNQueens(8))
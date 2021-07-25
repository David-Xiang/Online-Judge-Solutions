# LeetCode 51
# N-Queens
# Backtracing

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.backtrace(n, 0, [], ans)
        return ans

    def backtrace(self, n, now_row, used, ans):
        if now_row == n:
            grid = [] 
            for col in used:
               char_list = ['.'] * n
               char_list[col] = 'Q'
               grid.append("".join(char_list))
            ans.append(grid)
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
    print(Solution().solveNQueens(1))
    print(Solution().solveNQueens(4))
    print(len(Solution().solveNQueens(8)))
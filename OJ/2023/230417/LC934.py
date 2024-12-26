
import collections
from typing import Deque, List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[1])
        sx, sy = 0, 0
        for sx in range(rows):
            for sy in range(cols):
                if grid[sx][sy] == 1:
                    break
            if grid[sx][sy] == 1:
                break
        
        visited = [[False for _ in range(rows)] for _ in range(cols)]
        q = collections.deque()
        q.append((sx, sy))
        visited[sx][sy] = True
        border = self.getBorder(grid, visited, q)
        
        return self.flood(grid, visited, border)
    
    def getBorder(self, grid: List[List[int]], visited: List[List[bool]], q: Deque) -> Deque:
        border = collections.deque()
        while len(q) > 0:
            x, y = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 1:
                        q.append((nx, ny))
                    else:
                        border.append((nx, ny))
        return border
        
    def flood(self, grid: List[List[int]], visited: List[List[bool]], q: Deque) -> int:
        ans = 1
        while len(q) > 0:
            level = len(q)
            for _ in range(level):
                x, y = q.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        if grid[nx][ny] == 1:
                            return ans
                        q.append((nx, ny))
            ans = ans + 1
        return ans


if __name__ == "__main__":
    print(Solution().shortestBridge(grid = [[0,1],[1,0]]))
    print(Solution().shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
    print(Solution().shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
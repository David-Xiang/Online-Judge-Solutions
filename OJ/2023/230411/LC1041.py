# LeetCode 1041
# Robot Bounded In Circle
# Simulation

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        loc = [0, 0, 0]
        instructions = instructions * 4
        for i in instructions:
            if i == 'G':
                loc = self.go(loc)
            elif i == 'L':
                loc = self.turnLeft(loc)
            elif i == 'R':
                loc = self.turnRight(loc)
        return loc[0] == 0 and loc[1] == 0
    
    def go(self, loc: list[int]) -> list[int]:
        dir = loc[2]
        delta = [[0, 1],[1, 0], [0, -1], [-1, 0]]
        return [loc[0] + delta[dir][0], loc[1] + delta[dir][1], dir]
    
    def turnLeft(self, loc: list[int]) -> list[int]:
        return [loc[0], loc[1], (loc[2] + 3) % 4]
    
    def turnRight(self, loc: list[int]) -> list[int]:
        return [loc[0], loc[1], (loc[2] + 1) % 4]

if __name__ == '__main__':
    print(Solution().isRobotBounded('GG'))
    print(Solution().isRobotBounded('GGLLGG'))
    print(Solution().isRobotBounded('GL'))
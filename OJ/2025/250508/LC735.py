#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 小行星碰撞
#

# @lc code=start
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        to_left = []
        to_right = []
        for a in asteroids:
            if a > 0:
                to_right.append(a)
                continue
            while len(to_right) > 0 and to_right[-1] < -a:
                to_right.pop()
            if len(to_right) == 0:
                to_left.append(a)
                continue
            if to_right[-1] == -a:
                to_right.pop()
        return to_left + to_right
# @lc code=end

if __name__ == "__main__":
    print(Solution().asteroidCollision([5,10,-5]))
    print(Solution().asteroidCollision([8,-8]))
    print(Solution().asteroidCollision([10,2,-5]))
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1:
            if maxDoubles == 0:
                ans = ans + target - 1
                target = 1
            elif target % 2 == 1:
                target = target - 1
                ans = ans + 1
            else:
                target = target // 2
                maxDoubles = maxDoubles - 1
                ans = ans + 1
        return ans


if __name__ == '__main__':
    print(Solution().minMoves(5, 0))
    print(Solution().minMoves(19, 2))
    print(Solution().minMoves(10, 4))
    print(Solution().minMoves(766972377, 92))

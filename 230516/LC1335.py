from typing import List

INT_MAX = 1e9


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        dp = [[INT_MAX for jobs in range(len(jobDifficulty))]
              for date in range(d)]
        for date in range(0, d):
            for job in range(len(jobDifficulty)):
                diff = jobDifficulty[job]
                if date == 0:
                    if job == 0:
                        dp[date][job] = diff
                    else:
                        dp[date][job] = max(dp[date][job - 1], diff)
                else:
                    for t in range(job, date - 1, -1):
                        diff = max(diff, jobDifficulty[t])
                        dp[date][job] = min(
                            dp[date][job], dp[date - 1][t - 1] + diff)
        return dp[-1][-1] if dp[-1][-1] < INT_MAX else -1


if __name__ == '__main__':
    print(Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
    print(Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4))
    print(Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3))
    print(Solution().minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3))
    print(Solution().minDifficulty(jobDifficulty=[
          11, 111, 22, 222, 33, 333, 44, 444], d=6))

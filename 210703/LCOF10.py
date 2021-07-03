# LeetCodeOffer 10-I Easy
# Fibonacci
# Binary Exponentiation 矩阵快速幂

from typing import List
MOD = 1000000007

class Matrix:
    def __init__(self, n, m):
        self.mat = [[0] * m for i in range(n)]
        # Error: self.mat = [[0] * m] * n
        self.n = n
        self.m = m

    # A * B = A.__mul__(B) n * m (x) m * k
    def __mul__(self, matrix):
        k = matrix.m
        ans = Matrix(self.n, k)
        for i in range(self.n):
            for j in range(k):
                for t in range(self.m):
                    ans.mat[i][j] += self.mat[i][t] * matrix.mat[t][j]
                    ans.mat[i][j] %= MOD
        return ans

class Solution:
    def fib_slow(self, n: int) -> int:
        if n == 0:
            return 0
        A = Matrix(2, 2)
        A.mat = [[1, 1], [1, 0]]
        ans = Matrix(2, 1)
        ans.mat = [[1], [0]]
        for i in range(n - 1):
            ans = A * ans
        return ans.mat[0][0]

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        A = Matrix(2, 2)
        A.mat = [[1, 1], [1, 0]]
        A = self.power(A, n - 1)

        ans = Matrix(2, 1)
        ans.mat = [[1], [0]]
        ans = A * ans
        return ans.mat[0][0]

    def power(self, A, k):
        n = len(A.mat)
        ans = Matrix(n, n)
        for i in range(n):
            ans.mat[i][i] = 1
        while k > 0:
            if k % 2 == 1:
                ans = A * ans
            A = A * A
            k //= 2
        return ans


if __name__ == "__main__":
    print(Solution().fib(1))
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
    print(Solution().fib(5))
    print(Solution().fib(6))
    
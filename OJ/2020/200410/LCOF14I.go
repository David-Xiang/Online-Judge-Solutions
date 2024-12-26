package main

import "fmt"

// LeetCodeOffer 14-I Medium
// Cutting Rope
// Dynamic Programming
func LCOF14I() {
	fmt.Println(cuttingRope(2))
	fmt.Println(cuttingRope(10))
}

func cuttingRope(n int) int {
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		dp[i][i] = 1
	}

	for i := 1; i <= n; i++ {
		dp[0][i] = 1
	}

	for i := 1; i <= n; i++ {
		for j := i + 1; j <= n; j++ {
			for k := 1; j-k >= i-1; k++ {
				dp[i][j] = max(dp[i][j], k*dp[i-1][j-k])
			}
		}
	}

	res := 0
	for i := 2; i <= n; i++ {
		res = max(res, dp[i][n])
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

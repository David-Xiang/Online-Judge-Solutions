package main

import "fmt"

// LeetCodeOffer 14-II Medium
// Cutting Rope
// Greedy
// 数学敏感还是很重要
func LCOF14II() {
	fmt.Println(cuttingRope(2))
	fmt.Println(cuttingRope(10))
	fmt.Println(cuttingRope(120)) // return 953271190
}

func cuttingRope(n int) int {
	// 2 -> 2
	// 3 -> 3
	// 4 -> 2 2
	// 5 -> 3 2
	// 6 -> 3 3
	// 7 -> 3 2 2
	// 8 -> 3 3 2
	// 9 -> 3 3 3
	// 10 -> 3 3 2 2
	if n < 4 {
		// 特判2，3
		return n - 1
	}
	num3 := n / 3
	num2 := 0
	switch n % 3 {
	case 1:
		num3 -= 1
		num2 += 2
	case 2:
		num2 += 1
	}

	res := 1
	for i := 0; i < num2; i++ {
		res *= 2
	}
	for i := 0; i < num3; i++ {
		res = (res * 3) % 1000000007
	}
	return res
}

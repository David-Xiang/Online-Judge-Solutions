package main

import "fmt"

// LeetCodeOffer 17 Easy
// Print 1 to n
func LCOF17() {
	fmt.Println(printNumbers(1))
}

func printNumbers(n int) []int {
	l := 1
	for i := 0; i < n; i++ {
		l *= 10
	}
	res := make([]int, l-1)
	for i := 0; i < l-1; i++ {
		res[i] = i + 1
	}
	return res
}

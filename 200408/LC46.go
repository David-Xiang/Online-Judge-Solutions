package main

import "fmt"

// LeetCode 46 Medium
// Permutations
// Backtracing

var res [][]int
var use []bool
var prefix []int
var num []int

func LC46() {
	arr := []int{1, 2, 3}
	p := permute(arr)
	fmt.Print(p)
}

func permute(nums []int) [][]int {
	if len(nums) == 0 {
		return make([][]int, 0)
	}
	num = make([]int, len(nums))
	copy(num, nums)

	res = make([][]int, 0)
	use = make([]bool, len(nums))
	prefix = make([]int, 0)

	permuteInternal()
	return res
}

func permuteInternal() {
	if len(prefix) == len(num) {
		s := make([]int, len(prefix))
		copy(s, prefix)
		res = append(res, s)
	}
	for i := 0; i < len(use); i++ {
		if use[i] {
			continue
		}
		use[i] = true
		prefix = append(prefix, num[i])
		permuteInternal()
		use[i] = false
		prefix = prefix[:len(prefix)-1]
	}
}

package main

import (
	"fmt"
)

// LeetCodeOffer 11 Easy
// Find Minimum in Rotated Sorted Array
// Binary Search

func LCOF11() {
	arr := []int{3, 4, 5, 1, 2}
	fmt.Println(minArray(arr))
	arr = []int{2, 2, 2, 0, 1}
	fmt.Println(minArray(arr))
	arr = []int{1, 3, 5}
	fmt.Println(minArray(arr))
}

func minArray0(numbers []int) int {
	// 分治，慢一倍
	if len(numbers) == 1 {
		return numbers[0]
	} else if len(numbers) == 2 {
		return min(numbers[0], numbers[1])
	}

	mid := len(numbers) / 2
	if numbers[mid] < numbers[0] {
		return minArray(numbers[1 : mid+1])
	} else if numbers[0] < numbers[mid] {
		return min(numbers[0], minArray(numbers[mid+1:]))
	}

	return min(minArray(numbers[1:mid+1]), minArray(numbers[mid+1:]))
}

func minArray(numbers []int) int {
	// 迭代，快
	begin := 0
	end := len(numbers) - 1
	for begin < end {
		if numbers[begin] < numbers[end] {
			return numbers[begin]
		}
		mid := (begin + end) / 2
		if numbers[begin] < numbers[mid] {
			begin = mid + 1
		} else if numbers[mid] < numbers[begin] {
			end = mid
		} else {
			begin++
		}
	}
	return numbers[begin]
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

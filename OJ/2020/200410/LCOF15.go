package main

import "fmt"

// LeetCodeOffer 15 Easy
// Number of 1 Bits
// Bit Manipulation
func LCOF15() {
	fmt.Println(hammingWeight(15))
}

func hammingWeight(num uint32) int {
	res := uint32(0)
	for i := 0; i < 32; i++ {
		res += num & 1
		num >>= 1
	}
	return int(res)
}

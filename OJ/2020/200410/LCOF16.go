package main

import "fmt"

// LeetCodeOffer 16 Easy
// Pow(x, n)
// Math
func LCOF16() {
	fmt.Println(myPow(2.00000, 10))
	fmt.Println(myPow(2.10000, 3))
	fmt.Println(myPow(2.00000, -2))
}

func myPow(x float64, n int) float64 {
	if n < 0 {
		return myPow(1/x, -n)
	}

	exp2 := make([]float64, 33)
	exp2[1] = x
	for i := 2; i <= 32; i++ {
		exp2[i] = exp2[i-1] * exp2[i-1]
	}
	res := 1.0
	for i := 0; i < 32; i++ {
		if n&1 == 1 {
			res *= exp2[i+1]
		}
		n >>= 1
	}
	return res
}

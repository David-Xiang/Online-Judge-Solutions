package main

import (
	"fmt"
	"strings"
)

// LeetCode 22 Medium
// Generate Parentheses
// Backtracing

var s []byte
var sb strings.Builder
var res []string
var total int

func LC22() {
	p := generateParenthesis(3)
	fmt.Print(p)
}

func generateParenthesis(n int) []string {
	total = n
	s = make([]byte, 2*n)
	res = make([]string, 0)
	generateParenthesisInternal(0, 0)
	return res
}

func generateParenthesisInternal(leftUsed int, rightUsed int) {
	if leftUsed == total && rightUsed == total {
		sb.Reset()
		sb.Write(s)
		res = append(res, sb.String())
	}
	if leftUsed < total {
		s[leftUsed+rightUsed] = '('
		generateParenthesisInternal(leftUsed+1, rightUsed)
	}
	if rightUsed < leftUsed {
		s[leftUsed+rightUsed] = ')'
		generateParenthesisInternal(leftUsed, rightUsed+1)
	}
}

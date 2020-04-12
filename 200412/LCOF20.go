package main

import (
	"fmt"
)

const (
	space = 0
	abs   = 1
	num   = 2
	dot   = 3
	exp   = 4
	err   = 5
)

// 状态：
// 0 start，前缀空格
// 1 正负号
// 2 整数部分，可有前缀0
// 3 小数点
// 4 小数部分，若干位数字
// 5 e
// 6 指数正负号
// 7 指数部分，若干位数字
// 8 非法状态
// 9 后缀空格
// 接受状态有2，4，7，9

// 符号：
// 空格 0
// +- 1
// 数字 2
// 小数点 3
// e 4

// newState = jump[state][nextSymbol]
var jump = [10][5]int{
	{0, 1, 2, 3, 8}, // 前缀0跳转下一个
	{8, 8, 2, 3, 8}, // 正负号
	{9, 8, 2, 4, 5}, // 整数部分
	{8, 8, 4, 8, 8}, // 小数点
	{9, 8, 4, 8, 5}, // 小数部分
	{8, 6, 7, 8, 8}, // e
	{8, 8, 7, 8, 8}, // 指数正负号
	{9, 8, 7, 8, 8}, // 指数部分，若干位数字
	{8, 8, 8, 8, 8}, // 非法状态
	{9, 8, 8, 8, 8},
}

// LeetCodeOffer 20 Easy
// Valid Number
// Finite State Machine
func LCOF20() {
	printCase("2e10")      //"2e10" => true
	printCase(" -90e3   ") //" -90e3   " => true
	printCase(" 1e")       //" 1e" => false
	printCase("e3")        //"e3" => false
	printCase(" 6e-1")     //" 6e-1" => true
	printCase(" 99e2.5 ")  //" 99e2.5 " => false
	printCase("53.5e93")   //"53.5e93" => true
	printCase(" --6 ")     //" --6 " => false
	printCase("-+3")       //"-+3" => false
	printCase("95a54e53")  //"95a54e53" => false
	printCase(".1")        // true
	printCase("3.")        // true
	printCase(".")         // false
}
func printCase(s string) {
	fmt.Printf("%s: %t\n", s, isNumber(s))
}

func isNumber(s string) bool {
	state := 0
	for i := 0; i < len(s) && state != 8; i++ {
		t := symbolType(s[i])
		if t == err {
			return false
		}
		state = jump[state][t]
	}
	return state == 2 || state == 4 || state == 7 || state == 9
}

func symbolType(c uint8) int {
	if c == ' ' {
		return space
	} else if c == '+' || c == '-' {
		return abs
	} else if c >= '0' && c <= '9' {
		return num
	} else if c == '.' {
		return dot
	} else if c == 'e' {
		return exp
	}
	return err
}

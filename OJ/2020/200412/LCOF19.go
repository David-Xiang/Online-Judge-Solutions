package main

import "fmt"

// LeetCodeOffer 19 Hard
// Regular Expression Matching
// Dynamic Programming
func LCOF19() {
	fmt.Println(isMatch("aaa", "aaaa"))               // false
	fmt.Println(isMatch("aa", "a"))                   // false
	fmt.Println(isMatch("aa", "a*"))                  // true
	fmt.Println(isMatch("ab", ".*"))                  // true
	fmt.Println(isMatch("aab", "c*a*b"))              // true
	fmt.Println(isMatch("mississippi", "mis*is*p*.")) // false
	fmt.Println(isMatch("a", ".*..a*"))               // false
}

func isMatch(s string, p string) bool {
	// 将pattern拆分成可匹配的字符数组以及该字符数目是否可变的isstar[]
	pn := make([]uint8, 0)
	isstar := make([]bool, 0)
	var prev uint8 = '*'
	for i := range p {
		if p[i] != '*' {
			pn = append(pn, p[i])
			if prev != '*' {
				isstar = append(isstar, false)
			}
		} else {
			isstar = append(isstar, true)
		}
		prev = p[i]
	}
	if prev != '*' {
		isstar = append(isstar, false)
	}

	//dp[i][j]表示s[0~i-1] 匹配 p[0~j-1]，0行0列都是缓冲
	var dp = make([][]bool, len(s)+1)
	dp[0] = make([]bool, len(pn)+1)
	dp[0][0] = true
	for i := 1; i < len(pn)+1; i++ {
		dp[0][i] = dp[0][i-1] && isstar[i-1]
	}
	for i := 1; i < len(s)+1; i++ {
		dp[i] = make([]bool, len(pn)+1)
		dp[i][0] = false
		for j := 1; j < len(pn)+1; j++ {
			dp[i][j] = (dp[i-1][j-1] && equals(s[i-1], pn[j-1])) ||
				(dp[i-1][j] && equals(s[i-1], pn[j-1]) && isstar[j-1]) ||
				(dp[i][j-1] && isstar[j-1])
		}
	}

	return dp[len(s)][len(pn)]
}

func equals(a, b uint8) bool {
	if a == '.' || b == '.' {
		return true
	}
	return a == b
}

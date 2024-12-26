package main

import "fmt"

var table [][]byte
var visited [][]bool
var dirs = [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
var row, col int
var str string

// LeetCodeOffer 12 Medium
// Word Search
// Backtracing
func LCOF12() {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	fmt.Println(exist(board, "ABCCED"))
	fmt.Println(exist(board, "SEE"))
	fmt.Println(exist(board, "ABCB"))
}

func exist(board [][]byte, word string) bool {
	table = board
	str = word
	if len(str) == 0 {
		return true
	}

	row, col = len(board), len(board[0])
	visited = make([][]bool, row)
	for i, _ := range visited {
		visited[i] = make([]bool, col)
	}
	for i, row := range table {
		for j, col := range row {
			if col == str[0] {
				visited[i][j] = true
				if dfs(i, j, 1) {
					return true
				}
				visited[i][j] = false
			}
		}
	}
	return false
}

func dfs(i, j, next int) bool {
	if next == len(str) {
		return true
	}
	for _, dir := range dirs {
		nx, ny := i+dir[0], j+dir[1]
		if in(nx, ny) && table[nx][ny] == str[next] && !visited[nx][ny] {
			visited[nx][ny] = true
			if dfs(nx, ny, next+1) {
				return true
			}
			visited[nx][ny] = false
		}
	}
	return false
}

func in(i, j int) bool {
	return i < row && i >= 0 && j < col && j >= 0
}

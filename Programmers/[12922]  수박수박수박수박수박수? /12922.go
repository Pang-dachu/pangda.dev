package test

import "strings"

func solution(n int) string {
	res := strings.Repeat("수박", n/2)
	if n%2 == 1 {
		res += "수"
	}
	return res
}

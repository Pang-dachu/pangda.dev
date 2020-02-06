package test

import "sort"

func solution(strings []string, n int) []string {
	sort.Slice(strings, func(a, b int) bool {
		if strings[a][n] == strings[b][n] {
			return strings[a] < strings[b]
		}
		return strings[a][n] < strings[b][n]
	})
	return strings
}

package test

import (
	"sort"
	"strconv"
)

func solution(n int64) int64 {
	tmp := []byte(strconv.Itoa(int(n)))
	sort.Slice(tmp, func(a, b int) bool {
		return tmp[a] < tmp[b]
	})
	b, _ := strconv.Atoi(string(tmp))
	return int64(b)
}

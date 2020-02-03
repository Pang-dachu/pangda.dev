package main

import "sort"

func solution(array []int, commands [][]int) []int {
	answer := []int{}
	for _, i := range commands {
		var tmp = make([]int, i[1]-i[0]+1)
		copy(tmp, array[i[0]-1:i[1]])
		sort.Slice(tmp, func(a, b int) bool {
			return tmp[a] < tmp[b]
		})
		answer = append(answer, tmp[i[2]-1])
	}
	return answer
}


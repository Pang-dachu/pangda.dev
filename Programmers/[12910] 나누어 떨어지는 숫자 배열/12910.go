package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(solution([]int{5, 9, 7, 10}, 5))
}

func solution(arr []int, divisor int) []int {
	answer := []int{}
	for _, v := range arr {
		if v%divisor == 0 {
			answer = append(answer, v)
		}
	}

	if len(answer) == 0 {
		answer = append(answer, -1)
	} else {
		sort.Ints(answer)
	}
	return answer
}

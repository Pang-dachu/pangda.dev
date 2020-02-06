package main

import (
	"fmt"
	"strings"
)

func main() {
	s := [...]string{"pPoooyY", "Pyy"}
	for _, v := range s {
		fmt.Println(solution(v))
	}
}

func solution(s string) bool {
	return strings.Count(strings.ToLower(s), "p") == strings.Count(strings.ToLower(s), "y")
}

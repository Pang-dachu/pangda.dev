package test

import "strconv"

func solution(seoul []string) string {
	for i, j := range seoul {
		if j == "Kim" {
			return "김서방은 " + strconv.Itoa(i) + "에 있다"
		}
	}
	return ""
}

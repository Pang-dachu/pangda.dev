package test

import "regexp"

func solution(s string) bool {
	return regexp.MustCompile("(^[0-9]{4}|[0-9]{6})$").MatchString(s)
}

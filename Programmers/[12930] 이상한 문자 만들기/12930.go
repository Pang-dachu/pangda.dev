package test


import "strings"

func solution(s string) string {
	var answer []string
	var tmp string
	for _, v := range strings.Split(s, " ") {
		for ii, vv := range v {
			if ii%2 == 0 {
				tmp += strings.ToUpper(string(vv))
			} else {
				tmp += strings.ToLower(string(vv))
			}
		}
		answer = append(answer, tmp)
        tmp = ""
	}
	return strings.Join(answer, " ")
}


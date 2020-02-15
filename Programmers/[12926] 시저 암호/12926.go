package test

func solution(s string, n int) string {
	result := make([]rune, len(s))
	offset := rune(n)
	for i, v := range s {
		if 'A' <= v && v <= 'Z' {
			result[i] = ((v + offset - 'A') % 26) + 'A'
		} else if 'a' <= v && v <= 'z' {
			result[i] = ((v + offset - 'a') % 26) + 'a'
		} else {
			result[i] = v
		}
	}
	return string(result)
}

package test

func solution(s string) string {
	return s[(len(s)-1)/2 : len(s)/2+1]
}

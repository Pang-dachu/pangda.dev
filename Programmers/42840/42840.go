package moketest

func solution(answers []int) []int {
	answer := []int{}

	pick1 := [...]int{1, 2, 3, 4, 5}
	pick2 := [...]int{2, 1, 2, 3, 2, 4, 2, 5}
	pick3 := [...]int{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}

	correct := [3]int{0, 0, 0}

	//정답 체크
	for i, v := range answers {
		if v == pick1[i%len(pick1)] {
			correct[0]++
		}
		if v == pick2[i%len(pick2)] {
			correct[1]++
		}
		if v == pick3[i%len(pick3)] {
			correct[2]++
		}
	}
	m := 0
	for i, e := range correct {
		if i == 0 || e > m {
			m = e
		}
	}
	for i, e := range correct {
		if e == m {
			answer = append(answer, i+1)
		}
	}
	return answer
}

package test

import (
	"math"
)

func solution(n int64) int64 {
	x := math.Sqrt(float64(n))
	if int((x*100))%100 != 0 {
		return -1
	} else {
		return int64(math.Pow(x+1, float64(2)))
	}
}

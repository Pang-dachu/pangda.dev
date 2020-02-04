#sqrt_find, 프로그래머스 정수 제곱근 판별
import math

n = int(input())
answer = 0

sqrt = math.sqrt(n)
print(sqrt)

answer = (sqrt+1)**2 if sqrt == int(sqrt) else -1

print (answer)
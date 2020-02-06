#프로그래머스, 소수찾기
import math

def solution(n):
    n = int(n)

    answer = 0
    s_root = int(math.sqrt(n))

    if n != 1 :
        for i in range(2,(n+1)) :
            for j in range(2,(s_root+1)) :
                if i % j == 0 : 
                    #2,3,5 같은 수가 나올경우 소수로 판별함
                    if( i == j ) :
                        answer += 1
                        break
                    #소수가 아닌 수들을 판별
                    break
                    #pass               
            else : 
                answer += 1
                continue

    return answer


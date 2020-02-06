#프로그래머스, 소수찾기, 중간 프린트문 첨부
import math

def solution(n):
    n = int(n)

    answer = 0
    s_root = int(math.sqrt(n))

    if n != 1 :
        for i in range(2,(n+1)) :
            print("========")
            print("i값 : ", i)
            print("=")
            for j in range(2,(s_root+1)) :
                print("j값 : ", j)
                if i % j == 0 : 
                    #2,3,5 같은 수가 나올경우 소수로 판별함
                    if( i == j ) :
                        answer += 1
                        print("현재 i값 %d는 소수입니다.   "%i)
                        break
                    #소수가 아닌 수들을 판별
                    print("현재 i값 %d는 소수가 아닙니다." %i)
                    break
                    #pass               
            else : 
                print("현재 i값 %d는 소수입니다.   "%i)
                answer += 1
                continue

    return answer

num = input()
prime_count = solution(num)

print("소수의 갯수는 : ",prime_count)

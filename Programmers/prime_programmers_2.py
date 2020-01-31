#프로그래머스 소수 판별, 에라토스테네스의 체
#import math

def solution (num) :
    answer = 0

    num = int(num)
    #리스트 선언, 0은 수가 아니기때문에 이부분 False
    isPrime = [False]
    #0을 제외한 뒷부분 num의 갯수만큼 True로 선언
    isPrime = isPrime + ([True]*num)
    #1도 판별 대상이 아니기때문에, False로 선언
    isPrime[1] = False

    for i in range(2,num):
        for j in range(2,num):
            if i*j <= num :
                if isPrime[i*j] :                       
                    isPrime[i*j] = False 
            else : break

    answer = isPrime.count(True)
    return int(answer)




num = input()

answer = solution(num)
print(answer)

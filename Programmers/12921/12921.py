from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0: return False
    return True

def solution(n):
    answer = 0
    for i in range(1, n + 1, 2):
        if is_prime(i):
            answer += 1
    return answer

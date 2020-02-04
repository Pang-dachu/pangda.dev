import math

def solution(n):
    answer = 0
    
    sqrt = math.sqrt(n)
    
    # x = 1 if condition else (else 조건일때 값)
    answer = (sqrt+1)**2 if sqrt == int(sqrt) else -1
    
    return answer
프로그래머스 - Level 1 - 정수 제곱근 판별
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/12934    
2. 문제    
<문제설명>      
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.   
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.    
<제한 사항>         
n은 1이상, 50000000000000 이하인 양의 정수입니다.      

3. 문제 소스 코드 작성      
```python
import math

def solution(n):
    answer = 0   
    sqrt = math.sqrt(n)
       
    answer = (sqrt+1)**2 if sqrt == int(sqrt) else -1
    
    return answer
```

4. 문제 풀이    
어떤 수의 제곱근을 구하는 sqrt 함수를 사용하기 위해 파이썬 math모듈 사용.      
문제 사용 형식은 아래의 조건식과 같다.      
```python
x = 0 if condition else 1  
```python
어떠한 수의 제곱근을 구한 값과 그 제곱근의 int값이 같은지 비교하는 방식을 사용하였음.  

프로그래머스 - Level 1 - 
-------------

1. 문제의 링크   
  https://programmers.co.kr/learn/courses/30/lessons/12928  

2. 문제    
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.   
    
<제한 사항>     
n은 0 이상 3000이하인 정수입니다.      

3. 문제 소스 코드 작성      
```python
def solution(num):
    answer = 0
    #전제조건을 이용하기 위해, 입력된 수의 절반을 사용할 예정
    #절반 이하인 수들의 리스트 생성
    num_list = [i for i in range(1,int(num//2)+1)]
    #약수들의 집합을 저장하는 factor_list
    factor_list = []
    #약수들을 구해서 리스트에 추가함.
    #약수는 num을 나누었을때, 나머지가 0인 수들이 됨.
    for i in range(int(num/2)) :
        if num%num_list[i] == 0 : factor_list.append(num_list[i]) 

    return num + sum(factor_list)
```

4. 문제 풀이    
시작하기전 전제조건으로 '어떤 수가 나와도 약수는 그 수의 절반을 '초과'하는 수는 없다.'     
    
전제조건을 이용하기 위해서, num_list는 입력받은 수의 절반까지의 값을 가지는 리스트를 생성한다.       
이어 약수들의 집합을 저장하는 factor_list를 선언하고,     
입력받은 수를 절반이하인 수들의 집합으로 나누어서, 나머지가 0일때, 입력받은 수의 약수가 되기 때문에,      
factor_list에 추가한다.
    
factor_list들의 값과 입력받은 수의 값들을 모두 더한 값을 반환한다.     


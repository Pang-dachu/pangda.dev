프로그래머스 - Level 1 - 서울에서 김서방 찾기      
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/12919 

2. 문제    
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.     
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.      
<제한조건>      
seoul은 길이 1 이상, 1000 이하인 배열입니다.     
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.      
Kim은 반드시 seoul 안에 포함되어 있습니다.            
<입출력 예>         

|seoul|return|
|----|-----|
|["Jane","kim"]|"김서방은 1에 있다."|

3. 문제 소스 코드 작성      
```python
def solution(seoul):
    answer = "김서방은 %d에 있다" %seoul.index("Kim")
    
    return answer
```

4. 문제 풀이    
https://hashcode.co.kr/questions/65/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EC%95%84%EC%9D%B4%ED%85%9C%EC%9D%98-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EC%B0%BE%EA%B8%B0    
파이썬에서 리스트 인덱스 값 찾는 내장함수 사용함.                

  

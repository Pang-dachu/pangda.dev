프로그래머스 - Level 1 - 수박수박수
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/12922   

2. 문제    
길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.     예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.     
<제한조건>      
 n은 길이 10,000이하인 자연수입니다.        
<입출력 예>        

|array|return|
|----|-----|
|3|"수박수"|
|4|"수박수박"|  
          
3. 문제 소스 코드 작성      
```python
from itertools import chain, repeat

def solution(n):
    word = ["수","박"]
    temp = list(chain.from_iterable(repeat(word, int(n))) )
    answer = ''.join(temp[:n])
    
    return answer
```

4. 문제 풀이    
intertools의 chain과 repeat를 이용해서, 수박수박수가 반복되는 리스트 생성함.       
이후 입력받은 수만큼 리스트 슬라이싱 후 문자열 변환 후 출력함.             

  

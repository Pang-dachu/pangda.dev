프로그래머스 - Level 1 - 2016년
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/12901    

2. 문제    
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.    
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.    
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.     

<제한조건>  
2016년은 윤년입니다.   
2016년 a월 b일은 실제로 있는 날입니다.   
(13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)    

3. 문제 소스 코드 작성      
```python
def solution(a, b):
    days_plus = [0,3,6,0,3,5,1,3,6,2,4,0,2]
    answer = ''

    b = int(b) + int(days_plus[int(a)])

    #요일 판별
    if b % 7 == 0 : answer =  "MON"
    elif b % 7 == 1 : answer =  "TUE"
    elif b % 7 == 2 : answer =  "WED"
    elif b % 7 == 3 : answer =  "THU"

    elif b % 7 == 4 : answer =  "FRI"
    elif b % 7 == 5 : answer =  "SAT"
    elif b % 7 == 6 : answer =  "SUN"

    return answer
```

4. 문제 풀이    
각 월의 요일에 해당하는 수를 7로 나누었을때, 나머지 값을 이용해서 구한다.         
days_plus 리스트는 13의 크기를 가지는데, 리스트의 0번째는 0을 넣고
1부터 12까지 접근 및 인식하기에 용이하게 설정하였다.     
    
입력한 월을 기준으로 판단하여, days_plus 리스트에 들어있는 값을 일이라는 변수에 더한다.  

  

프로그래머스 - Level 1 - 완주하지 못한 선수
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/42576    
2. 문제     
<문제 설명>
수많은 마라톤 선수들이 마라톤에 참여하였습니다.  
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.   

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의    이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

<제한사항>  
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.    
completion의 길이는 participant의 길이보다 1 작습니다.   
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.  
참가자 중에는 동명이인이 있을 수 있습니다.    
3. 문제 소스 코드 작성  
```python
import collections

def solution(participant, completion):
    answer = ''.join(list(collections.Counter(participant) - collections.Counter(completion)))
    return answer 
```
4. 문제 풀이    
파이썬의 collection 모듈을 사용하였음.      
여러가지 형식이 있으나
collections.Counter를 사용하면 'hash' 가능한 객체를 카운ㅡ하는 dictionary 형태로 변환하며, 카운팅이 가능하다.  
이어 list()함수를 이용해서, dictionary 형태의 자료를 list 형으로 변경하고.
.join() 함수를 이용하여, 문자열 형태로 변경하여 저장한다.    

이후 answer 출력하는 것으로 문제 완료함.  
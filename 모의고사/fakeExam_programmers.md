프로그래머스 - Level 1 - 모의고사
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/42840    

2. 문제    
수포자는 수학을 포기한 사람의 준말입니다.         
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.   
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.      
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...    
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...  
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...  
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,   
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.    
<제한사항>      
시험은 최대 10,000 문제로 구성되어있습니다.     
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.       
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.               
<입출력 예>     
|answer|return|
|[1,2,3,4,5]|[1]|
|[1,3,2,4,2]|[1,2,3]|
<입출력 예 설명>      
수포자 1은 모든 문제를 맞혔습니다.        
수포자 2는 모든 문제를 틀렸습니다.        
수포자 3은 모든 문제를 틀렸습니다.            
    
3. 문제 소스 코드 작성      
```python
from itertools import chain, repeat

def solution(answers):
    answer = []
    #학생의 점수
    score = [0,0,0]

    answer_len = len(answers)

    #학생이 제출하는 답안의 패턴
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]

    #학생들의 답을 저장하는 리스트 생성
    stu_list1 = list(chain.from_iterable(repeat(stu1, int(len(answers)/len(stu1))+1)))
    stu_list2= list(chain.from_iterable(repeat(stu2, int(len(answers)/len(stu2))+1)))
    stu_list3 = list(chain.from_iterable(repeat(stu3, int(len(answers)/len(stu3))+1)))    

    #입력된 답안의 길이만큼 학생들의 답을 저장하는 리스트 슬라이싱.
    stu_list1 = stu_list1[:answer_len]
    stu_list2 = stu_list2[:answer_len]
    stu_list3 = stu_list3[:answer_len]   

    #리스트 완전 탐색을 이용한 비교
    for i in range(len(answers)):
        if answers[i] == stu_list1[i]:
            score[0] += 1
        if answers[i] == stu_list2[i]:
            score[1] += 1
        if answers[i] == stu_list3[i]:
            score[2] += 1                 

    max_score = max(score)
    for i in range(len(score)):
        if score[i] == max_score :
            answer.append(i+1)     

    return answer
```

4. 문제 풀이       
1. score 리스트에 학생 1,2,3 의 맞춘 문제의 갯수를 저장할 것임.    
2. answer_len은 입력받은 answers의 길이를 알기위해 사용함.     
3. 학생 1,2,3의 답안 작성 패턴을 미리 작성해놓음.       
4. 학생들의 답을 저장하는 리스트를 생성한다. (itertools 사용함, 반복되는 값으로 리스트 생성하기)       
5. 완전 탐색을 이용하여 비교함.         
6. 가장 큰 점수를 가진 score 리스트의 값을 찾아 answer에 넘겨준뒤, 해당값 출력.       


  

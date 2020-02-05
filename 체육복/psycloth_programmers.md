프로그래머스 - Level 1 - 체육복  
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/42862    

2. 문제    
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.  
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.  
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.     
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.     
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.  

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,  
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,   체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.  

3. 문제 소스 코드 작성      
```python
def solution(n, lost, reserve):

    stu_list = [1]*n

    #체육복의 여분을 가지고 있는 학생들의 값을 2로 변경함
    for i in range(len(reserve)):
        stu_list[reserve[i]-1] = 2
    #체육복을 잃어버린 학생들의 값을 1제거 함
    for i in range(len(lost)) :
        stu_list[lost[i]-1] -= 1

    while True :
        #첫번째 학생이 한벌만 있을때,
        #if stu_list[0] == 1 : pass 
        #첫번째 학생이 두벌 일때
        if stu_list[0] == 2 :
            if stu_list[1] == 0 :
                stu_list[0] -= 1
                stu_list[1] += 1
            #elif stu_list[1] != 0 : pass

        #마지막 학생이 두벌 일때
        if stu_list[len(stu_list)-1] == 2 :
            if(stu_list[len(stu_list)-2]) == 0 :
                stu_list[len(stu_list)-1] -= 1
                stu_list[len(stu_list)-2] += 1

        #그외의 학생들
        for i in range(1,len(stu_list)-1): 
            #if stu_list[i] == 1 : pass
            if stu_list[i] == 2 :
                if(stu_list[i-1] == 1) : pass
                if(stu_list[i+1] == 1) : pass

                if(stu_list[i-1]) == 0:
                    stu_list[i] -= 1
                    stu_list[i-1] += 1
                    continue
                elif stu_list[i-1] != 0 and (stu_list[i+1]) == 0:
                    stu_list[i] -= 1
                    stu_list[i+1] += 1
                    continue
        break


    answer = stu_list.count(1) + stu_list.count(2)
    return answer
```

4. 문제 풀이    
stu_list에 학생수 +1 만큼의 리스트를 생성한다. 
(0번째 리스트 요소를 만들어 놓음으로써, 리스트 인덱스와 학생 번호를 일치시키기 위함.)  
각 리스트의 요소는 1로 설정하여, 처음에는 체육복을 한벌씩 가지고 있는 것으로 설정함.   
    
체육복 여분을 가지고 있는 학생의 값은 2로, 잃어버린 학생의 값은 0으로 1 만큼 증감 시킨다.  
    
예외처리로 첫번쨰 학생과 마지막 학생을 처리하는데,    
첫번째 학생이 2벌을 가지고 있을때, 자신의 오른쪽을 확인해서 오른쪽의 값이 0이면, 체육복을 빌려주는 처리를 함.    
마지막 학생은 2벌을 가지고 있으면, 자신의 왼쪽을 확인해서, 왼쪽의 값이 0이면, 체육복을 빌려주는 처리를 함.     
    
전체적인 처리방식은 2벌을 가지고 있는 학생은, 자신의 왼쪽을 우선 확인하고, 왼쪽이 해당이 없을 경우 오른쪽을 확인후 처리함.     
    
체육복에 관한 처리를 완료하였으면, list에서 값이 1, 2인 요소를 찾아 count()함수를 이용해서 갯수를 확인하고     
그 값을 반환한다.      


  

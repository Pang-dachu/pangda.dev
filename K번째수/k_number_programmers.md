프로그래머스 - Level 1 - K번째 수
-------------

1. 문제의 링크   
https://programmers.co.kr/learn/courses/30/lessons/42748    

2. 문제    
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.     
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면      
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.     
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.        
2에서 나온 배열의 3번째 숫자는 5입니다.        
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,       
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록       solution 함수를 작성해주세요.    
    
<입출력 예>
|array|commands|return|
|-----|--------|------|     
|[1,5,2,6,3,7,4]|[[2,5,3],[4,4,1],[1,7,3]]|[5,6,3]|     
    
<입출력 예 설명>      
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.     
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.      
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.      
        
3. 문제 소스 코드 작성      
```python
def solution(array, commands):
    answer = []

    #commans 리스트의 길이만큼 for 문 실행.
    for i in range(len(commands)) :
        #임시 리스트를 생성한 뒤에, 커맨드 리스트의 값을 꺼내, array 리스트 슬라이싱,
        #슬라이싱 후에 sorted 이용해서 정렬한것을 temp_list에 저장함
        #answer 리스트에 commands리스트의 k번째 수 append이용해서 저장
        temp_array = sorted(array[(commands[i][0]-1) : (commands[i][1])])
        answer.append(temp_array[(commands[i][2])-1])
    return answer
```

4. 문제 풀이    
소스코드내 주석으로 풀이 설명 하였음.       
추가)sorted() 함수는 리스트 내의 요소를 정렬해주는 함수임.       

  

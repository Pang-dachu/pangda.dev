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
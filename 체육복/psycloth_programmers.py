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
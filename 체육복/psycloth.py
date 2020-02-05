#프로그래머스, 체육복 문제 


#학생 수 만큼의 크기를 가지는 리스트 생성, 초기값은 1로 설정한다.
stu_num = int(input())
stu_list = [1]*stu_num
#체육복을 잃어버린 학생의 리스트
lost = [2,4,7,8]
#체육복의 여분을 가지고 있는 학생의 리스트 
reserve = [3,6,9]

print(stu_list)

print("체육복  여분 파악 ")
#reserver 학생들의 값을 1증가
for i in range(len(reserve)):
    stu_list[reserve[i]-1] +=1

print("=============")
print("배열의 마지막 요소 파악 :", stu_list[8])
print("stu_list[len(stu_list)-1] : ", stu_list[len(stu_list)-1])
print("stu_list[len(stu_list)-2] : ", stu_list[len(stu_list)-2])
print("=============")

print(stu_list)

print("체육복 분실")
#lost 학생들의 값을 1 제거함
for i in range(len(lost)) :
    stu_list[lost[i]-1] -= 1

print(stu_list)



while True :
    #첫번째 학생이 한벌만 있을때,
    if stu_list[0] == 1 : pass 
    #첫번째 학생이 두벌 일때
    elif stu_list[0] == 2 :
        if stu_list[1] == 0 :
            stu_list[0] -= 1
            stu_list[1] += 1
        elif stu_list[1] != 0 : pass

    #마지막 학생이 두벌 일때
    if stu_list[len(stu_list)-1] == 2 :
        if(stu_list[len(stu_list)-2]) == 0 :
            stu_list[len(stu_list)-1] -= 1
            stu_list[len(stu_list)-2] += 1

    #그외의 학생들
    for i in range(1,len(stu_list)-1): 
        if stu_list[i] == 1 : pass
        elif stu_list[i] == 2 :
            if(stu_list[i-1]) == 0:
                stu_list[i] -= 1
                stu_list[i-1] += 1
            elif stu_list[i-1] != 0 and (stu_list[i+1]) == 0:
                stu_list[i] -= 1
                stu_list[i+1] += 1
    break

print(stu_list)

answer = stu_list.count(1) + stu_list.count(2)
print(answer)



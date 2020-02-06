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
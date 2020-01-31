def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    tmp = [0, 0, 0]

    for index in range(len(answers)):
        if answers[index] == first[index % 5]:
            tmp[0] += 1
        if answers[index] == second[index % 8]:
            tmp[1] += 1
        if answers[index] == third[index % 10]:
            tmp[2] += 1

    for index in range(len(tmp)):
        if tmp[index] == max(tmp):
            answer.append(index + 1)
    return answer
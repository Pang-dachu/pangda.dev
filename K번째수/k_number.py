#프로그래머스 k번째 수 구하기.

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
answer = []

#리스트 스플릿
# i = 0,1,2
for i in range(int(len(commands))) :
    temp_array = sorted(array[(commands[i][0]-1) : (commands[i][1])])
    #(commands[i][2])-1
    answer.append(temp_array[(commands[i][2])-1])
    #temp_array.sort()
    print(temp_array)
    print(answer)
    print("======")
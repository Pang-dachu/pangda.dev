#코드업 3120 리모컨 문제
#절대값 구하는 함수
def absTem(target, tem):
    if(target >= 0 and tem >= 0):
        return abs(target - tem)
    elif(target < 0 and tem < 0):
        return abs(target - tem)
    elif( (target < 0 and tem >= 0 ) or (target>=0 and tem < 0)) :
        return abs(target)+abs(tem)

#횟수 계산 함수
def remote(var,count):
    count +=int((var/10))
    var = var%10

    while var >= 0:
        if(var == 5):
            var = 0
            count +=1 

        #1~3
        elif(var < 4 and var > 0) :
            var -= 1
            count += 1

        #예외처리 4,8,9
        elif(var == 9):
            var = 0
            count += 2
        elif(var == 8):
            var = 0
            count += 3
        elif(var < 8 and var >= 5):
            var -= 5
            count += 1
        elif(var == 4):
            var = 0
            count += 2

        elif(var == 0):
            break       
    return count

tem, target = input().split(" ")

target = int(target)
tem = int(tem)
count = 0

interval = absTem(target, tem)

num = remote(interval, count)
print(num)

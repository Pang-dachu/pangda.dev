def solution(a, b):
    days_plus = [0,3,6,0,3,5,1,3,6,2,4,0,2]
    answer = ''

    b = int(b) + int(days_plus[int(a)])

    #요일 판별
    if b % 7 == 0 : answer =  "MON"
    elif b % 7 == 1 : answer =  "TUE"
    elif b % 7 == 2 : answer =  "WED"
    elif b % 7 == 3 : answer =  "THU"

    elif b % 7 == 4 : answer =  "FRI"
    elif b % 7 == 5 : answer =  "SAT"
    elif b % 7 == 6 : answer =  "SUN"

    return answer
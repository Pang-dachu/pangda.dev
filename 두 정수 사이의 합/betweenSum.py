#프로그래머스, 두정수 사이의 합


def solution(a, b):
    num = sorted([a,b])
    answer = sum([i for i in range(num[0],num[1]+1)])
    return answer

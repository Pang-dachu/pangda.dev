def solution(s, n):
    answer = ''
    for i in s:
        if ord(i.upper()) + n > 90:
            answer += chr(ord(i) - 26 + n)
        elif i == " ":
            answer += " "
        else:
            answer += chr(ord(i) + n)
    return answer
def solution(s):
    #"".join(list) -> 리스트에서 문자열로
    answer = ''.join(sorted(list(s), reverse=True))
    return answer
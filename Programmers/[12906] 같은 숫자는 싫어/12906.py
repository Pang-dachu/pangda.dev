def solution(arr):
    answer = []
    answer.append(arr[0])
    for v in arr[1:]:
        if answer[-1] != v:
            answer.append(v)
    return answer
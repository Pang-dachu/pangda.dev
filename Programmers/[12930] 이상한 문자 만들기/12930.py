def solution(s):
    answer = []
    for word in s.split(' '):
        answer.append(''.join([v.upper() if i%2==0 else v.lower() for i, v in enumerate(word)]))
    return ' '.join(answer)
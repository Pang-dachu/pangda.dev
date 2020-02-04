#프로그래머스, 완주하지 못한 선수
import collections

def solution(participant, completion):
    answer = ''.join(list(collections.Counter(participant) - collections.Counter(completion)))
    return answer 


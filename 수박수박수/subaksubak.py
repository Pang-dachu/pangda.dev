 #프로그래머스, 수박수박수
from itertools import chain, repeat

def solution(n):
    word = ["수","박"]
    temp = list(chain.from_iterable(repeat(word, int(n))) )
    answer = ''.join(temp[:n])
    
    return answer
#전제 조건
#어떤 수가 나와도 약수는 그 수의 절반을 '초과'하는 수는 없다.

def solution(num):
    answer = 0
    #전제조건을 이용하기 위해, 입력된 수의 절반을 사용할 예정
    #절반 이하인 수들의 리스트 생성
    num_list = [i for i in range(1,int(num//2)+1)]
    #약수들의 집합을 저장하는 factor_list
    factor_list = []
    #약수들을 구해서 리스트에 추가함.
    #약수는 num을 나누었을때, 나머지가 0인 수들이 됨.
    for i in range(int(num/2)) :
        if num%num_list[i] == 0 : factor_list.append(num_list[i]) 

    return num + sum(factor_list)
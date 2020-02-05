#프로그래머스, 약수의 합 구하기

#전제 조건
#어떤 수가 나와도 약수는 그 수의 절반을 '초과'하는 수는 없다.
num = int(input())


num_list = [i for i in range(1,int(num//2)+1)]
#factor_list = [num]
factor_list = []
#num을 나누어서 약수 먼저 구하기 헤헤
for i in range(int(num//2)) :
    if num%num_list[i] == 0 : factor_list.append(num_list[i]) 

#answer = num + sum(factor_list)
print(num + sum(factor_list))


answer = num + sum([i for i in range(1, int(num // 2) +1 ) if num % i  == 0])
print("시발...;;", answer)
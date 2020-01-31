#2001 최소대금.py
def minFind(*arg) :
    price = None
    for i in range(0,len(arg[0])):  
        if(price is None):
            price = float(arg[0][i])
        elif(price < float(arg[0][i])) :
            continue
        elif(price > float(arg[0][i])) :
            price = float(arg[0][i])     
    return price

def solution(pasta, dirnk) :
    solution = pasta+drink+((pasta+drink)*0.1)
    return solution

menu = [0 for _ in range(5)]

for i in range(0,5) :
    menu[i] = input()

pasta = minFind(menu[0:3])
drink = minFind(menu[3:])

print(solution(pasta,drink))










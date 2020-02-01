def solution(n, lost, reserve):
    answer = 0
    # have suit number 
    have_suit= [1 for i in range(n + 1)]
    for i in lost: have_suit[i] -= 1
    for i in reserve: have_suit[i]  += 1
    for index, suit in enumerate(have_suit):
        if suit == 2:
            try:
                if have_suit[index-1] == 0:
                    have_suit[index-1] += 1
                    have_suit[index] -= 1
                elif have_suit[index+1] == 0:
                    have_suit[index+1] += 1
                    have_suit[index] -= 1
            except: pass
                    

    
    answer = have_suit.count(1) + have_suit.count(2) 

    return answer - 1
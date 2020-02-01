
def solution(a, b):
    wlist = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return wlist[  (sum(months[:a]) + b + 5)  % 7] 
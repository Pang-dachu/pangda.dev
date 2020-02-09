import re
def solution(s):
    if re.fullmatch('[0-9]+', s) and len(s) == (4 or 6):
        return True
    else:
        return False

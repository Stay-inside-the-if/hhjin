def solution(s):
    answer = True
    pCount = s.lower().count('p')
    yCount = s.lower().count('y')
    
    if pCount == 0 and yCount == 0 :
        return True
    elif pCount == yCount:
        return True
    else :
        return False
        
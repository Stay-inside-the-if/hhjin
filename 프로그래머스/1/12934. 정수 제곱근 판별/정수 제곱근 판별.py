def solution(n):
    answer = 0
    half_n = n ** 0.5
    if half_n.is_integer() == True :
        answer = (half_n+1) ** 2
    else :
        answer = -1
    return answer
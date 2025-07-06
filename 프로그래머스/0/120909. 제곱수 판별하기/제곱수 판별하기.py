import math
def solution(n):
    answer = 0
    flag = math.isqrt(n)
    if flag * flag == n :
        answer = 1
    else :
        answer = 2
    return answer
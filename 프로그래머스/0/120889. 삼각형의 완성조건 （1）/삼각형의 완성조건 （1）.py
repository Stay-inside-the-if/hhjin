def solution(sides):
    answer = 0
    maxL = max(sides)
    total = sum(sides) - maxL
    if maxL < total :
        answer = 1
    else :
        answer = 2
    return answer
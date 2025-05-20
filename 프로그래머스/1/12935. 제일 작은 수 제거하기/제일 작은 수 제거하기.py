def solution(arr):
    answer = []
    minValue = min(arr)
    
    for i in arr :
        if i != minValue:
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer
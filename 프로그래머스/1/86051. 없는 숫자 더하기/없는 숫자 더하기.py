def solution(numbers):
    answer = 0
    new = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers :
        if i in new :
            new[i] = 0
    for i in new :
        answer += i
        
    return answer
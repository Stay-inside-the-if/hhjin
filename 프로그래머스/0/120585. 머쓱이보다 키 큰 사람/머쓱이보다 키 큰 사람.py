def solution(array, height):
    answer = 0
    for p in array :
        if height < p :
            answer += 1
    return answer
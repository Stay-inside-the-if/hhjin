def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0 : #0,2,4,6...
            answer += '수'
        else :
            answer += '박'
    return answer
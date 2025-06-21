def solution(x, n):
    answer = []
    up = x
    for i in range(n):
        answer.append(up)
        up = x + up
    return answer
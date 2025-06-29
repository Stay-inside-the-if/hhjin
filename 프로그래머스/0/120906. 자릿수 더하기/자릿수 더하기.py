def solution(n):
    answer = 0
    while n > 0:
        j = n % 10
        answer += j
        n = n // 10
    return answer
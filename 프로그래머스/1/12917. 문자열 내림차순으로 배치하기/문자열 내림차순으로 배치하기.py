def solution(s):
    answer = ''
    news = sorted(s, reverse=True)
    for i in news:
        answer += i
    return answer
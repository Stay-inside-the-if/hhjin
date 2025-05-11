def solution(s):
    answer = ''
    length = len(s)
    n = length // 2
    if length % 2 == 0 : #배열의 길이가 짝수이면
        answer = s[n-1] + s[n]
    else :
        answer = s[n]

    return answer
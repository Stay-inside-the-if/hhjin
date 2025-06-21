def solution(s):
    answer = ''
    a = 0
    for i in s :
        if i == ' ':
            a = -1
            
        if a % 2 == 0 : #짝수이면
            answer += i.upper()
        else:
            answer += i.lower()
        a+=1
    return answer
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6 : #문자열의 길이 조건
        answer = True
        for i in s : #숫자 구성 조건
            if ord(i) <  48 or ord(i) > 57: #아스키코드가 0에서9에 포함되지 않으면 
                answer = False
                break;
    return answer
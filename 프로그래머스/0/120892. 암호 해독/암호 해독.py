def solution(cipher, code):
    answer = ''
    for p in range(len(cipher)):
        if (p+1) % code == 0 : #4의 배수
            answer += cipher[p]
        
    return answer
def solution(n):
    answer , b = 0 , 1
    for i in range(n) :
        answer, b = b, (answer + b) % 1234567
    
    return answer
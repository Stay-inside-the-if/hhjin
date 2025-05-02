def solution(x):
    answer = True
    totalSum = 0
    temp = x
    while (temp > 0) :
        totalSum += (temp % 10)
        temp //= 10
    
    if (x % totalSum != 0):
        answer = False
        
    return answer
def solution(n):
    answer = 0
    result = ''.join(sorted(str(n), reverse=True))  
    answer = int(result)    
    return answer
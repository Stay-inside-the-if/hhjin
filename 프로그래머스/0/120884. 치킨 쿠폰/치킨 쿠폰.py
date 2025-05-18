def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        service = chicken // 10 #서비스로 받는 치킨 수
        answer += service
        chicken = chicken % 10 + service
        
    return answer
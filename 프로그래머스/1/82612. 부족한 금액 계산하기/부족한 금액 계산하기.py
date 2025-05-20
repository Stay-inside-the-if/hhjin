def solution(price, money, count):
    answer = 0
    totalPrice = 0
    for i in range(1, count + 1) : #4번동안 놀이기구를 탐
        totalPrice += (i * price)
        
    if money >= totalPrice:
        answr =  0
    else:
        answer = abs(money - totalPrice)
    
    return answer
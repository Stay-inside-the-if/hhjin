def solution(hp):
    answer = 0
    answer += hp // 5 
    five = hp % 5 
    answer += five // 3 
    three = five % 3 
    answer += three // 1
    one = three % 1
    return answer
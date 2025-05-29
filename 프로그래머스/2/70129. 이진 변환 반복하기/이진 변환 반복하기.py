def solution(s):
    answer = []
    zerosu = 0
    rowsu = 0
    while(s != '1'):
        oneloop = []
        for i in s :
            if i not in '0':
                oneloop.append(i)
        zerosu += (len(s) - len(oneloop)) #0 제거 수
        rowsu += 1
        s = bin(len(oneloop))[2:] 
    answer.append(rowsu)
    answer.append(zerosu)
    return answer
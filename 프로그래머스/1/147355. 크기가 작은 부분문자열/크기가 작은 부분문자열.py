def solution(t, p):
    answer = 0
    arr = []
    for i in range(len(t)):
        if (i+len(p)) > len(t) :
            break
        arr.append(t[i:i+len(p)])
        
    for i in arr :
        if int(p) >= int(i):
            answer += 1
    return answer
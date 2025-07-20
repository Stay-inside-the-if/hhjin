from itertools import combinations

def solution(n):
    answer = 0
    total = 0
    count = 0
    for i in range(1, n):
        total = 0
        for j in range(i, n):
            total += j
            if total == n :
                count += 1
            if total > n :
                break
    return count+1
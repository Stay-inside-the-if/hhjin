def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        rows = [] #행 
        for j in range(len(arr1[0])):
            rows.append(arr1[i][j] + arr2[i][j])
        answer.append(rows)
    return answer
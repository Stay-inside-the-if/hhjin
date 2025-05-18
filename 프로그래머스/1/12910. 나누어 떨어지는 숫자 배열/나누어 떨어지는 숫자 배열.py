def solution(arr, divisor):
    answer = []
    for i in arr :
        if i % divisor == 0 : 
            answer.append(i)
    
    answer.sort() #오름 차순으로 정렬
    
    if not answer: #파이썬에서 빈 리스트 []는 False처럼 평가
        answer.append(-1)
    return answer
def solution(arr):
    answer = []
    for i in arr :
        if not answer or i != answer[-1]: #answer문자열이 비어있거나 마지막 값이 i와 다르면 수행
            answer.append(i)
    return answer
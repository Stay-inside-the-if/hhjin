def solution(quiz):
    answer = []
    for i in quiz :
        left, right = i.split("=")
        left = eval(left)
        right = int(right)
        if left != right :
            answer.append("X")
        else :
            answer.append("O")
    return answer
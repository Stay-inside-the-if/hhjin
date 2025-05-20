def solution(s):
    answer = ''
    s_new = s.split() # ['1', '2', '3', '4'] 문자 리스트로 변환
    new_list = []
    for i in s_new :
        new_list.append(int(i)) # [1, 2, 3, 4]

    max_value = max(new_list)
    min_value = min(new_list)
    answer = str(min_value) + " " + str(max_value)
    return answer
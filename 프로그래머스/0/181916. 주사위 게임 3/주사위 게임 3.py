def solution(a, b, c, d):
    answer = 0
    nums = [a, b, c, d]
    dict_num = {}  #딕셔너리 생성
    for num in nums:
        if num in dict_num: 
            dict_num[num] += 1
        else:
            dict_num[num] = 1
    # print(dict_num)
    values = list(dict_num.values())
    keys = list(dict_num.keys())
    
    if len(values) == 1 : #모두 같은 문자라면
        answer = keys[0] * 1111
    
    elif len(values) == 2:
        if 3 in values:  # 3개, 1개
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            answer =  (10 * p + q) ** 2
        else:  # 2개씩 (2쌍)
            p, q = keys
            answer =  (p + q) * abs(p - q)
    elif len(values) == 3:  # 하나만 2개
        p = keys[values.index(2)]
        others = []
        for k in keys:
            if k != p:
                others.append(k)
        return others[0] * others[1]
    else :
        answer = min(nums)
        
        
    return answer
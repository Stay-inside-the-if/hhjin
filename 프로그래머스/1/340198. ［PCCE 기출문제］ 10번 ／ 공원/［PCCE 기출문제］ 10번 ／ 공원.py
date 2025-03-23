def solution(mats, park):
    answer = -1
    ## -1이 비어있는 자리 mats는 1차원 park는 2차원
    x = len(park)
    y = len(park[0]) ## 행 x , 열 y
    sum = 0

    for i in range(x) :
        for j in range(y) :
            if park[i][j] != "-1" :
                park[i][j] = 0
            else :
                park[i][j] = 1

    
    for k in range(len(mats)):
        size = mats[k]
        
        for a in range(x - size + 1): 
            for b in range(y - size + 1):  
                sum_val = 0 

                for i in range(size):
                    for j in range(size):
                        sum_val += park[a + i][b + j] 

                if sum_val == size * size: 
                    answer = max(answer, size)   
                     
            
    return answer
def solution(arr1, arr2):
    answer = []
    n1,m1 = len(arr1), len(arr1[0])
    n2,m2 = len(arr2), len(arr2[0])
    col_arr2 = []
    result_list = []
    
    # 1,4  3,3
    # 3,2  3,3
    # 4,1
    
    # 2,3,2  5,4,3
    # 4,2,4  2,4,1
    # 3,1,4  3,1,1
    
    for i in range(m2) :
        col = []
        for j in range(n2) :
            col.append(arr2[j][i])
        col_arr2.append(col)
    
    for i in arr1 :
        result_list = []
        for j in col_arr2 :
            result_list.append(sum(list(i*j for i,j in zip(i,j))))
    
        answer.append(result_list)
    
    return answer
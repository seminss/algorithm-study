def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)): 
        for j in range(len(arr2[0])): 
            for k in range(len(arr1[0])):
                answer[i][j]+=(arr1[i][k]*arr2[k][j])
    return answer

# 행열 곱셈 for 문으로 만드는 법
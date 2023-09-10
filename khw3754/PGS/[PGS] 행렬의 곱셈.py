def solution(arr1, arr2):
    answer = []

    # 편의상 arr을 변형시킴
    arr2 = list(map(list, zip(*arr2)))

    for a in arr1:
        # tmp == 한 행, 계산 후 answer(결과 행렬)에 넣어줌
        tmp = []
        for b in arr2:
            # t == 한 요소,  계산 후 tmp(행)에 넣어줌
            t = 0
            for i in range(len(a)):
                t += a[i] * b[i]
            tmp.append(t)
        answer.append(tmp)

    return answer
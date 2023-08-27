# 소인수분해로 딕셔너리에 추가

# 소인수분해하는 함수
def div(n):
    result = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result.append(i)
                n = n // i
                break
    return result


def solution(arr):
    max_dict = {}
    for a in arr:
        my_dict = {}
        # 각 소인수들의 개수의 리스트를 딕셔너리에 저장
        for d in div(a):
            if my_dict.get(d, -1) == -1:
                my_dict[d] = 1
            else:
                my_dict[d] += 1

        # max_dict에 없거나, 개수가 더 많은 소인수를 넣음
        for key, count in my_dict.items():
            if max_dict.get(key, -1) == -1:
                max_dict[key] = count
            elif max_dict[key] < count:
                max_dict[key] = count

    # 소인수들을 다 곱함
    result = 1
    for key, value in max_dict.items():
        result *= key ** value

    return result
def fac(n):
    return 1 if n == 1 else fac(n - 1) * n


def cal(sta, end, k, n):
    if n == 1:
        return [0]

    tmp = (end - sta + 1) // n
    ran = [(sta + tmp * i, sta + tmp * (i + 1)) for i in range(n)]  # [(1, 3), (3, 5), (5, 7)] 이런식으로 들어감
    for i, r in enumerate(ran):
        if r[0] <= k and k < r[1]:
            result = [i]
            result.extend(cal(r[0], r[1] - 1, k, n - 1))
            return result


def solution(n, k):
    answer = []

    nums = [i for i in range(1, n + 1)]
    result = cal(1, fac(n), k, n)
    print(result)

    for r in result:
        answer.append(nums[r])
        nums.pop(r)

    print(answer)
    return answer

solution(3,5)
# 진법 변환
def change(n, k):
    result = ""
    m = 0
    while k ** m <= n:
        m += 1
    m -= 1
    for i in range(m, -1, -1):
        for j in range(k - 1, -1, -1):
            if k ** i * j <= n:
                result += str(j)
                n -= k ** i * j
                break

    return result


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    count = 0

    nk = change(n, k)

    # P인 경우
    if '0' not in nk:
        if is_prime(int(nk)):
            count += 1
        ##### 문제: 0이 없을 때는 검사 후 count를 바로 반환해야한다.
        return count

    # 나머지 경우
    num_list = nk.split('0')
    for num in num_list:
        if num and is_prime(int(num)):
            count += 1

    return count
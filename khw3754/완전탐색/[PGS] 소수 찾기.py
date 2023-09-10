from itertools import permutations as permut


def is_prime(n):
    result = True
    if n == 0 or n == 1:
        return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            result = False
            break

    return result


def solution(numbers):
    answer = 0

    result = []
    for i in range(1, len(numbers) + 1):
        for j in set(permut(numbers, i)):
            result.append(int(''.join(j)))

    result = set(result)
    for r in result:
        print(r)
        if is_prime(r):
            answer += 1

    return answer
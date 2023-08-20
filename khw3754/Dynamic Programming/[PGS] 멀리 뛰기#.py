def solution(n):
    fib = [1, 2]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n - 1] % 1234567
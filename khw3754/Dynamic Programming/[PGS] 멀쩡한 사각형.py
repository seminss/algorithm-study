def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(w, h):
    answer = 1

    if w > h:
        w, h = h, w

    n = gcd(h, w)

    return w * h - (w // n + h // n - 1) * n
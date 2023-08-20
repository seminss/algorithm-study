from itertools import permutations as permut


def cal(expre, e):
    while e in expre:
        idx = expre.index(e)
        head, tail = expre[:idx], expre[idx + 1:]
        a, b = '', ''

        while head and (head[-1].isdigit() or head[-1] == '^'):
            a = head[-1] + a
            head = head[:-1]
        if a[-1] == '^':
            a = int(a[:-1]) * (-1)
        else:
            a = int(a)
        while tail and (tail[0].isdigit() or tail[0] == '^'):
            b += tail[0]
            tail = tail[1:]
        if b[-1] == '^':
            b = int(b[:-1]) * (-1)
        else:
            b = int(b)

        if e == '+':
            tmp = a + b
        elif e == '-':
            tmp = a - b
        elif e == '*':
            tmp = a * b

        if tmp >= 0:
            expre = head + str(tmp) + tail
        else:
            expre = head + str(tmp)[1:] + '^' + tail

    return expre


def solution(expression):
    answer = 0

    # 먼저 수식 안에 있는 연산자의 종류를 파악
    ex = []
    if '+' in expression:
        ex.append('+')
    if '-' in expression:
        ex.append('-')
    if '*' in expression:
        ex.append('*')

    can = list(permut(ex))
    results = []

    for c in can:
        expre = expression
        for e in c:
            expre = cal(expre, e)
        results.append(expre)

    # print(results)

    for i in range(len(results)):
        r = results.pop(0)
        if r[-1] != '^':
            results.append(int(r))
        else:
            results.append(int(r[:-1]))

    # print(results)

    return max(results)

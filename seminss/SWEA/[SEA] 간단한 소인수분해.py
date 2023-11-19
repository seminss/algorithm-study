# 10m
T = int(input())
standard = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    num = int(input())
    result = list()
    for s in standard:
        cnt = 0
        while num % s == 0:
            cnt += 1
            num = num // s
        result.append(str(cnt))
    print(f"#{test_case}", " ".join(result))
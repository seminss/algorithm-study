T = int(input())
for test_case in range(1, T + 1):
    result = set()
    num = int(input())
    cnt = 1 #갯수 세는 건 1부터!!
    while True:
        for s in str(num * cnt):
            result.add(s)
        if len(result) == 10:
            break
        cnt += 1

    print(f"#{test_case} {cnt * num}")

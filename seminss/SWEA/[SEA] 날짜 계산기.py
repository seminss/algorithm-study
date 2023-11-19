T = int(input())
# 40m
for test_case in range(1, T + 1):
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]  # else: 28
    fst_m, fst_d, scd_m, scd_d = map(int, input().split())

    if fst_m in thirty_one:
        result = 31 - fst_d
    elif fst_m in thirty:
        result = 30 - fst_d
    else:
        result = 28 - fst_d

    for m in range(fst_m + 1, scd_m):
        if m in thirty_one:
            result += 31
        elif m in thirty:
            result += 30
        else:
            result += 28

    if fst_m != scd_m:
        result += scd_d

    print(f'#{test_case} {result + 1}')

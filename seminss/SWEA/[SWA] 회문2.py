for test_case in range(10):
    t = int(input())
    maps = [str(input()) for _ in range(100)]
    result = 1
    for line in maps:
        for left in range(100):
            for right in range(left + 1, 100):
                for p in range((right - left + 1) // 2):
                    if line[left + p] != line[right - p]:
                        break
                    if p == (right - left + 1) // 2 - 1:
                        result = max(result, right - left + 1)

    for idx in range(100):
        for u in range(100):
            for d in range(u + 1, 100):
                for p in range((d - u + 1) // 2):
                    if maps[u + p][idx] != maps[d - p][idx]:
                        break
                    if p == (d - u + 1) // 2 - 1:
                        result = max(result, d - u + 1)

    print(f"#{t} {result}")
